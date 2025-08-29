from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import os
import sys

# Configurar las variables de entorno para Python
python_path = sys.executable
os.environ['PYSPARK_PYTHON'] = python_path
os.environ['PYSPARK_DRIVER_PYTHON'] = python_path

def spark_sql_operations():
    """
    Operaciones con Spark SQL y DataFrames.
    """
    print("Lección 4: Spark SQL y DataFrames")
    print("=" * 50)

    spark = SparkSession.builder \
        .appName("SparkSQLOperations") \
        .master("local[*]") \
        .getOrCreate()

    # Cargar datos de ejemplo (en este caso, creamos un DataFrame manualmente)
    data = [("Juan", 25), ("María", 30), ("Pedro", 35), ("Luisa", 40)]
    columns = ["nombre", "edad"]
    df = spark.createDataFrame(data, columns)

    print("DataFrame original:")
    df.show()

    # Registrar el DataFrame como vista temporal
    df.createOrReplaceTempView("personas")

    # Consulta SQL
    result_sql = spark.sql("SELECT * FROM personas WHERE edad > 30")
    print("Resultado de consulta SQL (edad > 30):")
    result_sql.show()

    # UDF (User Defined Function)
    def convertir_mayusculas(texto):
        return texto.upper()

    udf_mayusculas = udf(convertir_mayusculas, StringType())
    df_with_upper = df.withColumn("nombre_mayusculas", udf_mayusculas(df["nombre"]))
    print("DataFrame con UDF (nombres en mayúsculas):")
    df_with_upper.show()

    # Comparación de rendimiento: RDD vs DataFrame
    # Vamos a hacer un conteo de elementos con ambos y medir el tiempo (solo para demostración)
    import time

    # DataFrame
    start_time = time.time()
    count_df = df.count()
    time_df = time.time() - start_time

    # RDD
    start_time = time.time()
    count_rdd = df.rdd.count()
    time_rdd = time.time() - start_time

    print(f"Conteo con DataFrame: {count_df} (tiempo: {time_df:.6f} segundos)")
    print(f"Conteo con RDD: {count_rdd} (tiempo: {time_rdd:.6f} segundos)")
    print("Nota: En grandes volúmenes, DataFrames son más rápidos por el optimizador Catalyst.")

    spark.stop()


if __name__ == "__main__":
    spark_sql_operations()