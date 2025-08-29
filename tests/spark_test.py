import os
import sys
from pyspark.sql import SparkSession

# Configurar las variables de entorno
python_path = sys.executable
os.environ['PYSPARK_PYTHON'] = python_path
os.environ['PYSPARK_DRIVER_PYTHON'] = python_path

print(f"Python executable: {sys.executable}")
print(f"PYSPARK_PYTHON: {os.environ.get('PYSPARK_PYTHON')}")
print(f"PYSPARK_DRIVER_PYTHON: {os.environ.get('PYSPARK_DRIVER_PYTHON')}")

# Test de Spark
spark = SparkSession.builder \
    .appName("TestSparkFinal") \
    .master("local[*]") \
    .getOrCreate()

print("Spark session created successfully!")

# Crear un DataFrame simple
data = [("Test", 1), ("Spark", 2)]
df = spark.createDataFrame(data, ["Word", "Count"])
df.show()

spark.stop()