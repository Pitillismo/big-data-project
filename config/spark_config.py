import os
import sys
from pyspark.sql import SparkSession


def configure_spark():
    """Configura Spark con la versión correcta de Python"""
    python_path = sys.executable
    os.environ['PYSPARK_PYTHON'] = python_path
    os.environ['PYSPARK_DRIVER_PYTHON'] = python_path

    spark = SparkSession.builder \
        .appName("BigDataProject") \
        .master("local[*]") \
        .config("spark.executorEnv.PYSPARK_PYTHON", python_path) \
        .config("spark.executorEnv.PYSPARK_DRIVER_PYTHON", python_path) \
        .getOrCreate()

    return spark