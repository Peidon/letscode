from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, StructType, StringType, StructField, MapType
from pyspark.sql.functions \
    import udf, split, explode, upper, element_at, concat_ws, regexp_replace, collect_list, array_distinct, array_remove

from .common import *
from .descriptor import condition_description, filter_description

import logging
from datetime import datetime

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


def version_name(node_point_id: str) -> str:
    i = node_point_id.rfind('_')
    return node_point_id[:i]


# query buyer bot tfe condition nodes & answer nodes in ID, SG, MY
query_branch_list = '''
select region, bot_id, node_point_id, node_type, node_id, version_name,
case
    when node_type = 3 then get_json_object(whole_node_config, '$.button_setting.value')
end as buttons,
case 
    when node_type = 2 then get_json_object(whole_node_config, '$.branch_list.value')
    when node_type = 3 then get_json_object(whole_node_config, '$.answer_branch_list.value')
end as branch_list
from {0}.shopee_tfe_dwd_taskbot_node_content_df_reg 
where region in('ID','SG','MY') 
and node_type in(2,3) 
and bot_id = 3
'''

b_id_path = {
    2: "$.shadow_config.value.condition_id",  # condition node
    3: "$.shadow_config.value.case_id",  # answer node
}


def branch_id(b: object, node_type: int) -> str:
    path = b_id_path.get(node_type)
    if path:
        a = get_value_by_path(b, path)
        if a and isinstance(a, str):
            return str(a)
    return ""


def get_buttons_text(buttons: object) -> list:
    if not isinstance(buttons, list):
        logger.info("get_buttons", type(buttons))
        return []
    return [b.get("button_text") for b in buttons]


def extract_context(c_rdd):
    used = c_rdd["used_variates"]
    variates_json = c_rdd["variates"]
    if not isinstance(used, dict):
        logger.info("conditions variates", type(used))

    variates = json.loads(variates_json)

    conditions = []
    for v_key in used:
        v_name = used.get(v_key)
        if v_name and v_key in variates:
            va = variates[v_key]
            if not isinstance(va, str) and \
                    not isinstance(va, int) and \
                    not isinstance(va, float) and \
                    not isinstance(va, bool):
                continue

            va_str = str(va)
            if isinstance(va, int) and ('date' in v_name or 'time' in v_name):
                dt_object = datetime.fromtimestamp(va)
                va_str = dt_object.strftime('%d-%m-%Y')

            conditions.append(str(v_name) + "=" + va_str)

    condition_expr = c_rdd.condition_rule.strip()
    if len(conditions) > 0 and condition_expr != "":
        condition_expr += ", " + ", ".join(conditions)

    if condition_expr == "":
        condition_expr = ", ".join(conditions)

    return (c_rdd.region,
            c_rdd.trace_id,
            c_rdd.session_id,
            c_rdd.dialogue_id,
            c_rdd.answer_node_point,
            condition_expr)


# extract conditions branches
def extract_branches(b_rdd):
    raw_data = b_rdd.branch_list
    b_list = []

    node_id = b_rdd["node_id"]
    node_type = b_rdd["node_type"]

    branch_list = []

    if isinstance(raw_data, str):
        try:
            branch_list = json.loads(str(raw_data))
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON: {e}")

    for b in branch_list:
        b_id = branch_id(b, int(node_type))

        b_name = node_id + "/" + b_id

        groups = get_value_by_path(b, "$.branch_rule.value.groups")
        if not isinstance(groups, list):
            continue

        ds = condition_description(list(groups))
        c_rule, used_v = filter_description(ds)

        b_list.append({
            "branch_name": b_name,
            "used_variates": used_v,
            "condition_rule": c_rule,
        })

    answer_buttons = []
    if int(node_type) == 3:
        answer_buttons = get_buttons_text(b_rdd.buttons)

    return (b_rdd.region,
            b_rdd.node_point_id,
            b_rdd.version_name,
            answer_buttons,
            b_list)


def process(schema: str):
    spark = SparkSession.builder. \
        appName("shopee.chatbot.tfe.buyer_bot.llm_context"). \
        enableHiveSupport(). \
        getOrCreate()

    ql = query_branch_list.format(schema)
    branch_df = spark.sql(ql)

    # spark = SparkSession.builder. \
    #     appName("shopee.chatbot.tfe.buyer_bot.llm_context"). \
    #     getOrCreate()
    #
    # branch_df = spark.read.option("header", True).csv("../tmp/node_content.csv")
    # branch_df.show()
    # csv json str is broken

    # Adjusted 'extract_branches' schema definition
    branch_schema = StructType([
        StructField("region", StringType(), True),
        StructField("node_point_id", StringType(), True),
        StructField("version_name", StringType(), True),
        StructField("answer_buttons", ArrayType(StringType()), True),
        StructField("branch_list", ArrayType(StructType([
            StructField("branch_name", StringType(), True),
            StructField("used_variates", MapType(StringType(), StringType()), True),
            StructField("condition_rule", StringType(), True),
        ])), True),
    ])

    # Apply the schema when converting RDD to DataFrame
    branch_rdd = branch_df.rdd.map(extract_branches)
    branch_df = spark.createDataFrame(branch_rdd, branch_schema)

    branch_df = branch_df.select("region", "version_name", explode(branch_df.branch_list).alias("branch"))
    branch_df = branch_df.select("region", "version_name", "branch.*")

    # query buyer taskbot reply conditions
    reply_conditions = spark.sql("select * from {0}.shopee_tfe_dwd_taskbot_reply_conditions_df_reg_live "
                                 "where bot_id = 3 and has_end = true".format(schema))
    # udf
    version_name_udf = udf(lambda x: version_name(x))

    conditions = reply_conditions.select(upper("region").alias("region"),
                                         "trace_id", "session_id", "dialogue_id", "variates",
                                         version_name_udf(reply_conditions.node_point_id).alias("version_name"),
                                         concat_ws("_",
                                                   reply_conditions.bot_id,
                                                   upper(regexp_replace(
                                                       element_at(
                                                           split(reply_conditions.traffic_path, ","), -1), r'/', '_'))).
                                         alias("answer_node_point"),
                                         explode(
                                             array_distinct(
                                                 split(reply_conditions.traffic_path, ","))).
                                         alias("branch_name"),
                                         )

    df = conditions.filter(conditions.branch_name != 'root')

    df = df.join(branch_df, (df.region == branch_df.region) &
                 (df.version_name == branch_df.version_name) &
                 (df.branch_name == branch_df.branch_name)). \
        drop(df.region). \
        drop(df.version_name). \
        drop(df.branch_name)

    c_rdd = df.rdd.map(extract_context)

    c_schema = StructType([
        StructField("region", StringType(), True),
        StructField("trace_id", StringType(), True),
        StructField("session_id", StringType(), True),
        StructField("dialogue_id", StringType(), True),
        StructField("answer_node_point", StringType(), True),
        StructField("condition_expr", StringType(), True),
    ])
    result_df = c_rdd.toDF(schema=c_schema)

    condition_ctx = "condition_context"
    result_df = result_df. \
        groupBy("region", "session_id", "dialogue_id", "answer_node_point"). \
        agg(collect_list(result_df.condition_expr).alias(condition_ctx))

    target_hive_tab = "{0}.shopee_tfe_dwd_taskbot_llm_context_df__reg_live".format(schema)

    result_df.select("region", "session_id", "dialogue_id", "answer_node_point",
                     array_distinct(array_remove(result_df.condition_context, "")).alias(condition_ctx)).\
        write. \
        mode("overwrite"). \
        partitionBy("region"). \
        saveAsTable(target_hive_tab)

    spark.stop()
