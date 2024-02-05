import pyspark
from pyspark.sql import SparkSession


# source hive table
def taskbot_hive_tab(schema: str) -> str:
    return "{0}.tf_taskbot_mid_da_hive".format(schema)


def category_hive_tab(schema: str) -> str:
    return "{0}.tf_category_mid_da_hive".format(schema)


def flow_hive_tab(schema: str) -> str:
    return "{0}.tf_flow_mid_da_hive".format(schema)


def node_hive_tab(schema: str) -> str:
    return "{0}.tf_node_mid_da_hive".format(schema)


from .common import *


def button_count(x: str) -> int:
    return x.count("button_id")


import re


def rich_text_function_type(x: str) -> str:
    o = json.loads(x)
    p_lis = find_json_obj(o, "rich_text", JsonPath.ROOT.value)

    function_type = []
    for p in p_lis:
        v = get_value_by_path(o, p)
        if not isinstance(v, str):
            continue
        m = {
            "add_parameter": v.count("variable:"),
            "insert_link": len(re.findall("<a\s+href=\"http[s]?:.*?\"", v)),
            "upload_image": len(re.findall("<img\s+src=\"http[s]?:.*?\"", v)),
        }
        function_type.append(m)

    return json.dumps(function_type)


def intent_id_list(x: str) -> str:
    ans_ops = get_json_obj(x, "$.nlu_setting.value.answer_options")

    if not isinstance(ans_ops, list):
        return ""

    id_list = []
    options = list(ans_ops)
    for op in options:
        intent_id = op.get("taskbot_nlu_intent_id")
        id_list.append(str(intent_id))

    return ",".join(id_list)


def intent_name_list(x: str) -> str:
    ans_ops = get_json_obj(x, "$.nlu_setting.value.answer_options")

    if not isinstance(ans_ops, list):
        return ""

    id_list = []
    options = list(ans_ops)
    for op in options:
        id_list.append(op.get("taskbot_nlu_intent_name"))

    return ",".join(id_list)


def clarification_round(x: str) -> int:
    clarify_round = get_json_obj(x, "$.nlu_setting.value.taskbot_nlu_intent_clarification")

    if not isinstance(clarify_round, list):
        return 0

    return len(list(clarify_round))


def key_info(x: str) -> str:
    ans_ops = get_json_obj(x, "$.nlu_setting.value.answer_options")

    if not isinstance(ans_ops, list):
        return ""

    lis = []
    options = list(ans_ops)
    for op in options:
        k_info = {
            "intent_id": op.get("taskbot_nlu_intent_id"),
            "intent_name": op.get("taskbot_nlu_intent_name"),
            "key_information": op.get("entity_setting"),
        }

        lis.append(k_info)

    return json.dumps(lis)


def clarification_failed_action(x: str) -> str:
    action = get_json_obj(x, "$.reclarification_setting.value.failed_action")
    return failed_action_name.get(action)


failed_action_name = {
    1: "jump to next node",
    2: "drop"
}


def interaction_name(x: str) -> str:
    """
    spark udf for extract interaction name
    :param x: content json str
    :return: interaction name
    """
    content = json.loads(x)
    if JsonPath.INTERACTION.value in content:
        interaction = content.get(JsonPath.INTERACTION.value)
        if not interaction:
            return ''
        if JsonPath.VALUE.value in interaction:
            v = interaction.get(JsonPath.VALUE.value)
            return interaction_type_map.get(v, Error.UNKNOWN.value)

    return ''


def card_type(x: str) -> str:
    """
    spark udf for extract card type name
    :param x: content json str
    :return: card type name
    """
    content = json.loads(x)
    if JsonPath.CARD_TYPE.value in content:
        card_type_val = content.get(JsonPath.CARD_TYPE.value)
        if not card_type_val:
            return ''
        if JsonPath.VALUE.value in card_type_val:
            v = card_type_val.get(JsonPath.VALUE.value)
            return card_type_name.get(v, Error.UNKNOWN.value)

    return ''


def order_card_style(x: str) -> str:
    """

    :param x: content json str
    :return: card style name
    """
    content = json.loads(x)
    if JsonPath.ORDER_CARD_STYLE.value in content:
        val = content.get(JsonPath.ORDER_CARD_STYLE.value)
        if not val:
            return ''
        if JsonPath.VALUE.value in val:
            v = val.get(JsonPath.VALUE.value)
            return card_style_name.get(v, Error.UNKNOWN.value)

    return ''


card_style_name = {
    0: "Old Carousel",
    1: "New Carousel",
    2: "Big Carousel",
    3: "Vertical List",
    4: "Two-Row Carousel"
}

interaction_type_map = {
    1: "button selection",
    2: "card",
    3: "popup",
    4: "order selector",
    5: "variation",
    6: "item collector"
}

card_type_name = {
    1: "order",
    2: "topup",
    3: "withdrawal",
    4: "food driver",
    5: "food buyer"
}


# taskbot table join category table
def category_taskbot_sql(schema: str) -> str:
    return '''
select  bot_id,
        taskbot.region, 
        c.l1_category_id, 
        c.l1_category_name, 
        c.l2_category_id, 
        c.l2_category_name, 
        c.l3_category_id, 
        c.l3_category_name ,
        taskbot_id,
        taskbot_name, 
        taskbot.update_time as taskbot_update_time
from {0} taskbot
left join (
    select l3.category_id as l3_category_id, l2.category_id as l2_category_id, l1.category_id as l1_category_id,
        l3.category_name as l3_category_name, l2.category_name as l2_category_name, l1.category_name as l1_category_name
    ,l1.region as region
    from {1} l3
    left join {1} l2 ON l2.category_id = l3.parent_id
    left join {1} l1 ON l1.category_id = l2.parent_id
) c 
on c.l3_category_id = taskbot.category_id
and c.region = taskbot.region
where taskbot.is_deleted=0
'''. \
        format(taskbot_hive_tab(schema), category_hive_tab(schema))


def flow_sql(schema: str) -> str:
    return '''
SELECT  taskbot_id,
        version, 
        region,
        flow_id as version_name, 
        version_desc as version_description,
        flow_status as version_status, 
        update_user as version_operator,
        update_time as version_update_time 
FROM {0}
WHERE is_delete=0
'''. \
        format(flow_hive_tab(schema))


def node_sql(schema: str) -> str:
    return '''
SELECT  flow_id,  
        node_point_id, 
        node_id, 
        node_type,
        region,
        content as whole_node_config
FROM {0}
'''. \
        format(node_hive_tab(schema))


from pyspark.sql.functions import get_json_object, udf


def extract_from_content(node: pyspark.sql.dataframe) -> pyspark.sql.dataframe:
    """
    extract data from node content
    :param node: node data frame
    :return: node with all columns data frame
    """
    interaction_udf = udf(lambda z: interaction_name(z))
    card_type_udf = udf(lambda z: card_type(z))
    card_style_udf = udf(lambda z: order_card_style(z))
    intent_id_udf = udf(lambda z: intent_id_list(z))
    intent_name_udf = udf(lambda z: intent_name_list(z))
    clarification_round_udf = udf(lambda z: clarification_round(z))
    key_info_udf = udf(lambda z: key_info(z))
    clarification_failed_action_udf = udf(lambda z: clarification_failed_action(z))
    button_count_udf = udf(lambda z: button_count(z))
    rich_text_function_type_udf = udf(lambda z: rich_text_function_type(z))

    return node.withColumn("interaction_type_id", get_json_object(node.whole_node_config, "$.interaction.value")). \
        withColumn("interaction_type_name", interaction_udf(node.whole_node_config)). \
        withColumn("card_type_id", get_json_object(node.whole_node_config, "$.card_type.value")). \
        withColumn("card_type_name", card_type_udf(node.whole_node_config)). \
        withColumn("order_card_style_id", get_json_object(node.whole_node_config, "$.order_card_style.value")). \
        withColumn("order_card_style_name", card_style_udf(node.whole_node_config)). \
        withColumn("taskbot_intent_id", intent_id_udf(node.whole_node_config)). \
        withColumn("taskbot_intent_name", intent_name_udf(node.whole_node_config)). \
        withColumn("clarification_round", clarification_round_udf(node.whole_node_config)). \
        withColumn("key_information", key_info_udf(node.whole_node_config)). \
        withColumn("button_count", button_count_udf(node.whole_node_config)). \
        withColumn("rich_text_function_type", rich_text_function_type_udf(node.whole_node_config)). \
        withColumn("clarification_failed_action", clarification_failed_action_udf(node.whole_node_config)). \
        withColumn("allow_input_by_texting", get_json_object(node.whole_node_config, "$.input_setting.value"
                                                                                     ".allow_input_by_texting"))


def process(schema: str):
    spark = SparkSession.builder.appName("tfe_node_configs_tracking.cs").enableHiveSupport().getOrCreate()

    # query category & taskbot data frame
    taskbotDF = spark.sql(category_taskbot_sql(schema))

    # read flow table
    flowDF = spark.sql(flow_sql(schema))

    # flow join taskbot
    flow_taskbot_join = flowDF. \
        join(taskbotDF,
             (taskbotDF.taskbot_id == flowDF.taskbot_id) & (taskbotDF.region == flowDF.region), "left"). \
        drop(flowDF.taskbot_id). \
        drop(flowDF.region)

    # read node table
    nodeDF = spark.sql(node_sql(schema))

    # node join flow_taskbot_join
    tf_node = nodeDF. \
        join(flow_taskbot_join,
             (flow_taskbot_join.version_name == nodeDF.flow_id) & (flow_taskbot_join.region == nodeDF.region), "left"). \
        drop(nodeDF.flow_id). \
        drop(nodeDF.region)

    # target hive table
    target_hive_tab = "{0}.shopee_tfe_dwd_taskbot_node_content_df_reg".format(schema)
    extract_from_content(tf_node).write. \
        mode("overwrite"). \
        partitionBy("region"). \
        saveAsTable(target_hive_tab)

    spark.stop()
