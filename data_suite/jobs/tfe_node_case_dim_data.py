import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, StructType, StringType, StructField, IntegerType, BooleanType


def node_sql(schema: str) -> str:
    # source hive table
    node_hive_tab = "{0}.tf_node_mid_da_hive".format(schema)

    node_sq = '''
    SELECT  flow_id,  
            node_point_id, 
            node_id, 
            region,
            bot_id,
            content
    FROM {0}
    '''. \
        format(node_hive_tab)
    return node_sq


from .common import *
from pyspark.sql.functions import explode, udf, from_json


def branches(x: str) -> str:
    b = get_json_obj(x, "$.answer_branch_list.value")
    if not isinstance(b, list):
        return "[]"
    b_list = list(b)

    lis = []
    for case in b_list:
        case_id = get_value_by_path(case, "$.shadow_config.value.case_id")
        case_name = get_value_by_path(case, "$.name.value")
        card_setting = get_value_by_path(case, "$.card_setting.value.type")
        related_intent = get_value_by_path(case, "$.related_intents.value")
        action_type = get_value_by_path(case, "$.answer_action.value.action")
        feed_back = get_value_by_path(case, "$.advance_setting.value.feedback")
        end_tag = get_value_by_path(case, "$.advance_setting.value.end_tag")
        m = {
            "case_id": case_id,
            "case_name": case_name,
            "card_setting": card_setting,
            "related_intent": related_intent,
            "action_type": action_type,
            "feed_back": feed_back,
            "end_tag": end_tag
        }
        lis.append(m)

    return json.dumps(lis)


def node_case(node: pyspark.sql.dataframe) -> pyspark.sql.dataframe:
    branch_udf = udf(lambda z: branches(z), StringType())
    branch_schema = ArrayType(
        StructType(fields=[
            StructField("case_id", StringType()),
            StructField("case_name", StringType()),
            StructField("card_setting", IntegerType()),  # 1=_, 2=Timeline 3=Courier
            StructField("related_intent", ArrayType(IntegerType())),
            StructField("action_type", StringType()),
            StructField("feed_back", BooleanType()),
            StructField("end_tag", BooleanType())
        ])
    )

    branch_col = "branch_list"
    case_df = node.withColumn(branch_col, branch_udf(node.content))
    case_df = case_df.withColumn(branch_col, from_json(case_df.branch_list, branch_schema))
    case_df = case_df.select("*", explode(case_df.branch_list).alias("branch"))

    return case_df.select("*", "branch.*"). \
        drop("branch"). \
        drop(case_df.content). \
        drop(branch_col)


def process(schema: str):
    spark = SparkSession.builder. \
        appName("tfe_node_case_dim.cs"). \
        enableHiveSupport(). \
        getOrCreate()
    # sc = spark.sparkContext

    # read node table
    node_df = spark.sql(node_sql(schema))

    # target hive table
    target_hive_tab = "{0}.shopee_tfe_node_case_dim_df_reg".format(schema)

    node_case(node_df).write. \
        mode("overwrite"). \
        partitionBy("region"). \
        saveAsTable(target_hive_tab)

    spark.stop()
