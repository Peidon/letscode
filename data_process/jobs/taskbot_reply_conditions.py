import re

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, udf, from_json
from pyspark.sql.types import ArrayType, StructType, StringType, StructField, IntegerType, BooleanType, MapType

import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# from data_process.jobs.common import *
from .common import *

variate_data = {
    1: 'int_val',
    2: 'float_val',
    3: 'string_val',
    4: 'bool_val',
    5: 'struct_val',
    6: 'struct_val',
    7: 'struct_val',
    8: 'string_val',
    9: 'int_val',
    10: 'string_val',
    11: 'struct_val',
    12: 'array_val'
}


def variates_info(x: str) -> str:
    vs = get_json_obj(x, "$.variate")

    if not isinstance(vs, dict):
        return json.dumps(vs)

    m = dict()
    for k in vs:
        va = vs[k]
        if 'is_empty' in va and va['is_empty']:
            m[k] = None
            continue

        if 'type' not in va:
            logger.info("no type field in variate info : {}".format(k))
            continue

        data_type = va['type']
        field = variate_data.get(data_type)
        if field in va:
            m[k] = va[field]
        else:
            m[k] = None

    return json.dumps(m)


def track_nodes(x: str) -> dict:
    buffer_json_str = get_json_obj(x, "$.buffer")
    buffer_json_str = str(buffer_json_str).replace("\\", "")
    path = get_json_obj(str(buffer_json_str), "$.traffic_recorder.path")

    node_branches = dict()
    for p in str(path).split(","):
        if p.lower() == "root":
            continue
        track = p.split("/")
        if len(track) > 0:
            node_branches[track[0]] = ""
        if len(track) > 1:
            node_branches[track[0]] = track[1]

    session_id = get_json_obj(x, "$.variate.session_id.string_val")
    dialogue_id = get_json_obj(x, "$.variate.dialogue_id.string_val")
    msgs = get_json_obj(x, "$.msgs")
    node_point_id = ""
    has_end = False

    if isinstance(msgs, list):
        for msg in list(msgs):

            is_end = get_value_by_path(msg, "$.is_end")
            if bool(is_end):
                has_end = True

            msg_config = get_value_by_path(msg, "$.msg_config")
            config_json_str = str(msg_config).replace("\\", "")
            if not is_json(config_json_str):
                continue

            np = get_json_obj(config_json_str, "$.node_point_id")
            if np:
                node_point_id = np

    return {
        "session_id": session_id,
        "dialogue_id": dialogue_id,
        "node_point_id": node_point_id,
        "has_end": has_end,
        "variates": variates_info(x),
        "traffic_path": path,
        "node_branches": node_branches,
    }


def extract_cid(line: str) -> str:
    region_prefix = 'Region:'
    cid_idx = line.find(region_prefix)
    if cid_idx >= 0:
        start = cid_idx + len(region_prefix)
        return line[start: start + 2]
    return ""


def extract_trace_id(line: str) -> str:
    trace_prefix = 'TraceId:'
    idx = line.find(trace_prefix)
    if idx >= 0:
        start = idx + len(trace_prefix)
        return line[start: start + len('5134483e108512de5f96bada924e1a02')]
    return ""


def extract_bot_id(line: str) -> int:
    pattern = r"BotID:(\d+)"
    match = re.search(pattern, line)
    if not match:
        return 0
    group = match.group()
    if len(group) > 0:
        gs = group.split(":")
        if len(gs) > 1:
            bot_id = gs[1]
            return int(bot_id)
    return 0


def extract_reply_conditions(log_info_data: pyspark.sql.dataframe) -> pyspark.sql.dataframe:
    conditions_udf = udf(lambda z: reply_conditions(z), StringType())
    conditions_schema = ArrayType(
        StructType(fields=[
            StructField("region", StringType()),
            StructField("trace_id", StringType()),
            StructField("bot_id", IntegerType()),
            StructField("session_id", StringType()),
            StructField("dialogue_id", StringType()),
            StructField("node_point_id", StringType()),
            StructField("variates", StringType()),
            StructField("node_branches", MapType(StringType(), StringType())),
            StructField("traffic_path", StringType()),
            StructField("has_end", BooleanType())
        ])
    )
    condition_col = "conditions"
    condition_alias = "condition"
    data = log_info_data.withColumn(condition_col, conditions_udf(log_info_data.value))
    data = data.withColumn(condition_col, from_json(data.conditions, conditions_schema))
    data = data.select("*", explode(data.conditions).alias(condition_alias))

    return data.select(condition_alias+".*")


def reply_conditions(info: str) -> str:
    res = extract_response_json(info)
    return json.dumps(res)


def extract_response_json(info: str) -> list:
    # remove \\ in json text
    info = info.replace("\\\"", "\"")
    info = info.replace("\\\\", "\\\\\\")

    responses = []
    lines = info.split('deadline=')
    for line in lines:

        response_prefix = 'response='
        start_index = line.find(response_prefix)
        end_index = line.find(',sps_code=0')
        if start_index < 0 or start_index >= end_index:
            continue

        # Extract the JSON string from this point
        json_str = line[start_index + len(response_prefix): end_index]
        try:
            # Attempt to parse the JSON string
            o = track_nodes(json_str)
            # Add Base info
            bot_id = extract_bot_id(line)
            cid = extract_cid(line)  # region
            trace_id = extract_trace_id(line)
            o["bot_id"] = bot_id
            o["region"] = cid
            o["trace_id"] = trace_id

            responses.append(o)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON: {e}")

    return responses


# local debug
if __name__ == '__main__':
    with open("../../tmp/info.log", "r") as log_data:
        extract_response_json(log_data.read())


def process(schema: str):
    spark = SparkSession.builder.\
        appName("chatbot.tfe.taskbot.reply_conditions.cs").\
        enableHiveSupport().getOrCreate()

    # select log info
    log_info_data = spark.sql('''select * from {0}.log_data_taskbot_reply__reg_continuous_s0_live where 
from_unixtime(_timestamp, 'yyyy-MM-dd') = date_sub(current_timestamp(), 1)'''.format(schema))

    # target hive table
    target_hive_tab = "{0}.shopee_tfe_dwd_taskbot_reply_conditions_df_reg_live".format(schema)

    reply_condition = extract_reply_conditions(log_info_data)

    reply_condition.write. \
        mode("append"). \
        partitionBy("region"). \
        saveAsTable(target_hive_tab)

    spark.stop()
