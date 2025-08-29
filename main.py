from src.lesson_1.big_data_concepts import describe_big_data
from src.lesson_2.spark_architecture import describe_spark_architecture
from src.lesson_3.rdd_operations import rdd_operations
from src.lesson_4.spark_sql_operations import spark_sql_operations
from src.lesson_6.mllib_operations import mllib_example
import os

# Configuración global de Python para Spark
os.environ['PYSPARK_PYTHON'] = r'C:\Users\cmill\PycharmProjects\big_data_project\.venv1\Scripts\python.exe'
os.environ['PYSPARK_DRIVER_PYTHON'] = r'C:\Users\cmill\PycharmProjects\big_data_project\.venv1\Scripts\python.exe'


def run_all_lessons():
    print("Proyecto de Big Data con Apache Spark")
    print("=" * 50)

    # Lección 1: Big Data
    describe_big_data()
    input("\nPresiona Enter para continuar a la Lección 2...")

    # Lección 2: Spark Architecture
    describe_spark_architecture()
    input("\nPresiona Enter para continuar a la Lección 3...")

    # Lección 3: RDD Operations
    rdd_operations()
    input("\nPresiona Enter para continuar a la Lección 4...")

    # Lección 4: Spark SQL
    spark_sql_operations()
    input("\nPresiona Enter para continuar a la Lección 6...")

    # Lección 6: MLlib
    mllib_example()


def run_streaming_only():
    from src.lesson_5.spark_streaming import spark_streaming_example
    spark_streaming_example()


def main():
    print("Selecciona una opción:")
    print("1. Ejecutar todas las lecciones")
    print("2. Ejecutar solo Streaming (Lección 5)")

    choice = input("Tu elección (1 o 2): ")

    if choice == "1":
        run_all_lessons()
    elif choice == "2":
        run_streaming_only()
    else:
        print("Opción no válida. Saliendo.")


if __name__ == "__main__":
    main()