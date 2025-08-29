from pyspark.sql import SparkSession


def describe_spark_architecture():
    """
    Describe la arquitectura de Spark y sus componentes.
    """
    print("Lección 2: Apache Spark")
    print("=" * 50)

    # Inicializar una sesión de Spark
    spark = SparkSession.builder \
        .appName("SparkArchitecture") \
        .master("local[*]") \
        .getOrCreate()

    # Obtener información del contexto
    sc = spark.sparkContext
    print("Información de la aplicación Spark:")
    print(f"Nombre de la aplicación: {sc.appName}")
    print(f"Versión de Spark: {sc.version}")
    print(f"Modo de ejecución: {sc.master}")

    # Descripción de los componentes
    components = {
        "Driver": "Coordina la ejecución de la aplicación y mantiene el estado.",
        "Executors": "Procesan las tareas en los nodos del clúster.",
        "Cluster Manager": "Gestiona los recursos del clúster (Standalone, YARN, Mesos, Kubernetes)."
    }

    print("\nComponentes de la arquitectura de Spark:")
    for component, desc in components.items():
        print(f"- {component}: {desc}")

    # Módulos de Spark que usaremos
    print("\nMódulos de Spark utilizados en el proyecto:")
    modules = [
        "Spark Core: API fundamental y motor de ejecución.",
        "Spark SQL: Procesamiento de datos estructurados con SQL y DataFrames.",
        "Spark Streaming: Procesamiento de datos en tiempo real.",
        "MLlib: Machine Learning escalable."
    ]
    for module in modules:
        print(f"- {module}")

    spark.stop()


if __name__ == "__main__":
    describe_spark_architecture()