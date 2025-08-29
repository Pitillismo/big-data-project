from pyspark.sql import SparkSession


def test_spark():
    spark = SparkSession.builder \
        .appName("TestSpark") \
        .master("local[*]") \
        .getOrCreate()

    data = [("Test", 1), ("Spark", 2)]
    df = spark.createDataFrame(data, ["Word", "Count"])
    df.show()

    spark.stop()


if __name__ == "__main__":
    test_spark()