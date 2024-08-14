from pyspark.sql import SparkSession

from .taskbot_reply_conditions import extract_reply_conditions
from .llm_taskbot_context import version_name,extract_context

# functions
from pyspark.sql.functions import udf, split, explode, upper, element_at, concat_ws, regexp_replace,collect_list
from pyspark.sql.types import StructType, StringType, StructField, MapType


def process(log_data: str):
    spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

    # extract from log_data
    df = spark.createDataFrame([(1707122826, log_data)], ["_timestamp", "value"])
    reply_conditions = extract_reply_conditions(df)

    # udf
    version_name_udf = udf(lambda x: version_name(x))

    branch_alias = "branch_name"
    branches = reply_conditions.select(upper("region").alias("region"),
                                       "variates",
                                       version_name_udf(reply_conditions.node_point_id).alias("version_name"),
                                       concat_ws("_",
                                                 reply_conditions.bot_id,
                                                 upper(regexp_replace(
                                                     element_at(
                                                         split(reply_conditions.traffic_path, ","), -1), r'/', '_')
                                                 )).alias("answer_node_point"),
                                       explode(split(reply_conditions.traffic_path, ",")).alias(branch_alias),
                                       )

    # condition_branch schema:
    schema = StructType([
        StructField("region", StringType(), True),
        StructField("version_name", StringType(), True),
        StructField("branch", StructType([
            StructField("branch_name", StringType(), True),
            StructField("used_variates", MapType(StringType(), StringType()), True),
            StructField("condition_rule", StringType(), True),
        ])),
    ])
    # region, bot_id, version_name(e.g. SOP2_F2), node_type, branch_name(node_id/case_name),
    # condition_rule(expression, string type), used_variates(map<key, name>)
    condition_branch_data = ([
        ("ID", "SOP2_F26", {"branch_name": "SOP2_Node4321/condition_2",
                            "used_variates": {"order_id": "Order ID", "refund_status": "Refund status"},
                            "condition_rule": "order_id > 0"}),
        ("ID", "SOP2_F26", {"branch_name": "SOP2_Node4465/condition_1",
                            "used_variates": {"dialogue_id": "Dialogue ID", "session_id": "Session ID"},
                            "condition_rule": "order_id > 0"}),
        ("ID", "SOP2_F26", {"branch_name": "SOP2_Node4469/condition_3",
                            "used_variates": {"user_id": "User ID"},
                            "condition_rule": "get_order.create_time + current_time > 86400"})])

    cb_df = spark.createDataFrame(condition_branch_data, schema)
    cb_df = cb_df.select("region", "version_name", "branch.*")
    cb_df.show(truncate=False)

    df = branches.filter(branches.branch_name != 'root').dropDuplicates(["region", "version_name", branch_alias]).\
        filter(branches.version_name == 'SOP2_F26')

    df.show(truncate=100)

    df = df.join(cb_df, (df.region == cb_df.region) &
                 (df.version_name == cb_df.version_name) &
                 (df.branch_name == cb_df.branch_name)).drop(df.region).drop(df.version_name).drop(df.branch_name)
    df.show(truncate=20)

    c_rdd = df.rdd.map(extract_context)

    c_schema = StructType([
        StructField("region", StringType(), True),
        # StructField("trace_id", StringType(), True),
        # StructField("session_id", StringType(), True),
        # StructField("dialogue_id", StringType(), True),
        StructField("answer_node_point", StringType(), True),
        StructField("condition_expr", StringType(), True),
    ])
    result_df = c_rdd.toDF(schema=c_schema)
    result_df = result_df.\
        groupBy("region", "answer_node_point").agg(collect_list(result_df.condition_expr).alias("condition_context"))
    result_df.show(truncate=False)

    # debug unit time
    # spark.sql("select from_unixtime(1707122826, 'yyyy-MM-dd'), date_sub(current_timestamp(), 1)").show()
