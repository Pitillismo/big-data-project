from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.linalg import Vectors
import os
import sys


def mllib_example():
    """
    Ejemplo de MLlib: clasificación binaria con datos sintéticos.
    """
    print("Lección 6: MLlib - Machine Learning")
    print("=" * 50)

    # Configurar las variables de entorno para Python
    python_path = sys.executable
    os.environ['PYSPARK_PYTHON'] = python_path
    os.environ['PYSPARK_DRIVER_PYTHON'] = python_path

    spark = SparkSession.builder \
        .appName("MLlibExample") \
        .master("local[*]") \
        .getOrCreate()

    # Crear datos sintéticos para clasificación binaria
    data = [
        (Vectors.dense([0.1, 0.2, 0.3, 0.4, 0.5]), 0.0),
        (Vectors.dense([0.5, 0.4, 0.3, 0.2, 0.1]), 1.0),
        (Vectors.dense([0.2, 0.3, 0.4, 0.5, 0.6]), 0.0),
        (Vectors.dense([0.6, 0.5, 0.4, 0.3, 0.2]), 1.0),
        (Vectors.dense([0.3, 0.4, 0.5, 0.6, 0.7]), 0.0),
        (Vectors.dense([0.7, 0.6, 0.5, 0.4, 0.3]), 1.0),
        (Vectors.dense([0.4, 0.5, 0.6, 0.7, 0.8]), 0.0),
        (Vectors.dense([0.8, 0.7, 0.6, 0.5, 0.4]), 1.0)
    ]

    columns = ["features", "label"]
    df = spark.createDataFrame(data, columns)

    print("Dataset sintético para clasificación:")
    df.show()

    # Dividir datos
    train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

    # Definir el modelo de regresión logística
    lr = LogisticRegression(featuresCol="features", labelCol="label")

    # Entrenar el modelo
    model = lr.fit(train_data)

    # Realizar predicciones
    predictions = model.transform(test_data)
    predictions.select("features", "label", "prediction", "probability").show()

    # Evaluar el modelo
    evaluator = BinaryClassificationEvaluator(labelCol="label",
                                              rawPredictionCol="rawPrediction",
                                              metricName="areaUnderROC")
    auc = evaluator.evaluate(predictions)
    print(f"AUC del modelo: {auc}")

    # Guardar el modelo (opcional)
    try:
        model.write().overwrite().save("./models/synthetic_model")
        print("Modelo guardado en 'models/synthetic_model'")
    except Exception as e:
        print(f"Error al guardar el modelo (esperado en Windows): {str(e)[:100]}...")
        print("El modelo se entrenó correctamente pero no se pudo guardar debido a la configuración de Windows")
        print("En un entorno Linux/cloud, el modelo se guardaría correctamente")

if __name__ == "__main__":
    mllib_example()