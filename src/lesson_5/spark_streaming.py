from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
import os
import sys


def spark_streaming_example():
    """
    Ejemplo de Spark Streaming con socket.
    """
    print("Lección 5: Spark Streaming")
    print("=" * 50)

    # Configuración EXPLÍCITA de Python (CRUCIAL para Windows)
    python_path = sys.executable
    os.environ['PYSPARK_PYTHON'] = python_path
    os.environ['PYSPARK_DRIVER_PYTHON'] = python_path

    print(f"Python path configurado: {python_path}")

    spark = SparkSession.builder \
        .appName("SparkStreaming") \
        .master("local[*]") \
        .config("spark.executorEnv.PYSPARK_PYTHON", python_path) \
        .config("spark.executorEnv.PYSPARK_DRIVER_PYTHON", python_path) \
        .config("spark.pyspark.python", python_path) \
        .config("spark.pyspark.driver.python", python_path) \
        .getOrCreate()

    sc = spark.sparkContext
    sc.setLogLevel("ERROR")  # Reducir logs para mejor visibilidad
    ssc = StreamingContext(sc, 5)  # Intervalo de 5 segundos

    # Conectar al socket
    lines = ssc.socketTextStream("localhost", 9999)

    # Procesamiento del stream
    words = lines.flatMap(lambda line: line.split(" "))
    word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

    # Imprimir resultados
    word_counts.pprint()

    # Iniciar el streaming
    ssc.start()
    print("Streaming iniciado. Conectándose a localhost:9999")
    print("Para enviar datos, ejecuta en otra terminal: nc -lk 9999")
    print("Presiona Ctrl+C para detener")

    try:
        ssc.awaitTermination()
    except KeyboardInterrupt:
        print("\nDeteniendo streaming...")
        ssc.stop(stopSparkContext=True, stopGraceFully=True)


if __name__ == "__main__":
    spark_streaming_example()