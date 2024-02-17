from pyspark.sql import SparkSession

from .tfe_node_dim_data import extract_from_content
from .tfe_node_case_dim_data import node_case
from .data_examples import *
from .common import *


def process(_: str):
    spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
    df = spark.createDataFrame([(1, clarify_node_json_str), (2, clarify_fail_str)], ["id", "whole_node_config"])
    extract_from_content(df).show()
    b = spark.createDataFrame([(1, answer_node_str)], ["node_id", "content"])
    c = node_case(b)
    c.show()
    # print(c.branch_list)
    # print(c.schema)
    o = json.loads(clarify_node_json_str)
    p_lis = find_json_obj(o, "rich_text", JsonPath.ROOT.value)
    for p in p_lis:
        v = get_value_by_path(o, p)
        print(p + " : {" + v + "}")

    spark.sql("select from_unixtime(1707122826, 'yyyy-MM-dd'), date_sub(current_timestamp(), 0)").show()
