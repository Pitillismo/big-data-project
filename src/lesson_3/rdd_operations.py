from pyspark.sql import SparkSession
import os
import sys

# Configurar las variables de entorno para Python
python_path = sys.executable
os.environ['PYSPARK_PYTHON'] = python_path
os.environ['PYSPARK_DRIVER_PYTHON'] = python_path

def rdd_operations():
    """
    Operaciones con RDDs: transformaciones y acciones.
    """
    print("Lección 3: Procesamiento distribuido con RDDs")
    print("=" * 50)

    spark = SparkSession.builder \
        .appName("RDDOperations") \
        .master("local[*]") \
        .getOrCreate()

    sc = spark.sparkContext

    # Crear un RDD a partir de una lista
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    rdd = sc.parallelize(data, 4)  # 4 particiones

    print(f"Número de particiones: {rdd.getNumPartitions()}")
    print(f"Conteo de elementos: {rdd.count()}")
    print(f"Elementos: {rdd.collect()}")

    # Transformaciones
    # Filter: números pares
    rdd_filtered = rdd.filter(lambda x: x % 2 == 0)
    print(f"Filter (pares): {rdd_filtered.collect()}")

    # Map: multiplicar por 2
    rdd_mapped = rdd.map(lambda x: x * 2)
    print(f"Map (x2): {rdd_mapped.collect()}")

    # Distinct: eliminar duplicados
    rdd_distinct = rdd.distinct()
    print(f"Distinct: {rdd_distinct.collect()}")

    # SortBy: ordenar descendente
    rdd_sorted = rdd.sortBy(lambda x: x, ascending=False)
    print(f"SortBy (desc): {rdd_sorted.collect()}")

    # Union: unir con otro RDD
    rdd2 = sc.parallelize([11, 12, 13])
    rdd_union = rdd.union(rdd2)
    print(f"Union: {rdd_union.collect()}")

    # Acciones
    # Take: tomar los primeros 3
    print(f"Take(3): {rdd.take(3)}")

    # Mean: promedio
    print(f"Mean: {rdd.mean()}")

    # Stdev: desviación estándar
    print(f"Stdev: {rdd.stdev()}")

    # CountByValue: conteo de cada valor
    print(f"CountByValue: {rdd.countByValue()}")

    spark.stop()


if __name__ == "__main__":
    rdd_operations()