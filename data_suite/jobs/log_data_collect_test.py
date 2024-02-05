from pyspark.sql import SparkSession

from .llm_taskbot_data_source import extract_reply_conditions


def process(schema: str):
    spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
    df = spark.createDataFrame([(1707122826, schema)], ["_timestamp", "value"])
    extract_reply_conditions(df).show()