from pyspark import rdd
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StructType, StringType, StructField, ArrayType


def prefix_find(data: str, prefix: str, n: int) -> str:
    idx = data.find(prefix)
    if idx >= 0:
        start = idx + len(prefix)
        if n <= 0:
            return data[start:]
        return data[start: start + n]
    return ""


def range_find(data: str, prefix: str, suffix: str) -> str:
    start_index = data.find(prefix)
    end_index = data.find(suffix)
    if start_index < 0 or start_index >= end_index:
        return ""

    # Extract the JSON string from this point
    return data[start_index + len(prefix): end_index]


def str_list(data: str) -> list:
    return data.split(",")


import json


def json_list(data: str) -> list:
    if len(data) == 0:
        return []
    try:
        a = json.loads(data)
    except json.JSONDecodeError:
        return []
    return a


def last_node_point(path: list) -> str:
    if not path:
        return ''

    if len(path) <= 0:
        return ''
    last = path[len(path) - 1]
    if not isinstance(last, dict):
        return ''
    node_id = last.get('NodeID')
    branch_id = last.get('Branch')
    point_id = '{0}_{1}'.format(node_id, branch_id)
    return point_id.upper()


def extract_dialogue_states(log_data: rdd) -> [tuple]:
    data = log_data["value"]
    if not isinstance(data, str):
        return []

    lines = data.split("answer_rewriter")

    return filter(
        lambda x: x[2] != "" and x[3] != "",
        list(map(lambda item: (
            prefix_find(item, 'Region:', 2),
            prefix_find(item, 'session=', len('1209602234582438784')),
            prefix_find(item, 'dialogue id=', len('1227803051888802816')),
            last_node_point(json_list(range_find(item, 'path=', ',dialogue id='))),
            range_find(item, 'reply=', ',buttons='),
            str_list(range_find(item, 'buttons=[', '],conditions=')),
            str_list(range_find(item, 'conditions=[', '],rounds=')),
            json_list(range_find(item, 'rounds=', ',path=')),
            range_find(item, 'instance=', ',session'),
            prefix_find(item, 'TraceId:', len('5134483e108512de5f96bada924e1a02')),
            int(log_data["_timestamp"]),
            log_data["dt"],
        ), lines))
    )


def process(schema: str):
    spark = SparkSession.builder.appName("chatbot.tfe.taskbot.dst").enableHiveSupport().getOrCreate()
    df = spark.sql('''select * from {0}.log_data_taskbot_reply__reg_continuous_s0_live where from_unixtime(
    _timestamp, 'yyyy-MM-dd') = date_sub(current_timestamp(), 1)'''.format(schema))

    target_schema = StructType([
        StructField("region", StringType()),
        StructField("session_id", StringType()),
        StructField("dialogue_id", StringType()),
        StructField("node_point_id", StringType()),
        StructField("node_content", StringType(), True),
        StructField("buttons", ArrayType(StringType()), True),
        StructField("condition_list", ArrayType(StringType()), True),
        StructField("session_rounds", ArrayType(StructType([
            StructField("utterance", StringType(), True),
            StructField("create_method", StringType(), True),
            StructField("answer_list", ArrayType(StringType())),
        ])
        )),
        StructField("instance_id", StringType(), True),  # component service instance id
        StructField("trace_id", StringType()),
        StructField("timestamp", IntegerType()),
        StructField("_date", StringType())
    ])

    target_rdd = df.rdd.flatMap(extract_dialogue_states)
    result = target_rdd.toDF(schema=target_schema)

    target_hive_tab = "{0}.shopee_tfe_dwd_taskbot_llm_dataset_df__reg_live".format(schema)

    result.write. \
        mode("append"). \
        partitionBy("region"). \
        saveAsTable(target_hive_tab)

    spark.stop()
