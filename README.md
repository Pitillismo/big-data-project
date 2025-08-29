# Proyecto de Big Data con Apache Spark
## 📋 Descripción del Proyecto
Este proyecto implementa un pipeline completo de procesamiento de datos masivos utilizando Apache Spark. El sistema es capaz de manejar datos estructurados y no estructurados, tanto en procesamiento batch como en tiempo real, incluyendo machine learning escalable.

## 🎯 Objetivos Cumplidos
✅ Procesamiento distribuido de grandes volúmenes de datos

✅ Consultas SQL optimizadas con Spark SQL

✅ Procesamiento en tiempo real con Spark Streaming

✅ Machine Learning escalable con MLlib

✅ Integración de múltiples formatos de datos

✅ Arquitectura tolerante a fallos y escalable

## 🛠️ Tecnologías Utilizadas
### Apache Spark
Justificación: Spark fue elegido por su capacidad de procesamiento en memoria, soporte para múltiples lenguajes, y su ecosistema unificado que incluye Spark SQL, Spark Streaming y MLlib.

### Python (PySpark)
Justificación: PySpark permite integrar el poder de Spark con la simplicidad y popularidad de Python, facilitando el desarrollo y la integración con otras librerías de data science.

### WSL (Windows Subsystem for Linux)
Justificación: Para el procesamiento en streaming, WSL permite ejecutar netcat en un entorno Linux mientras se desarrolla en Windows.

### Formatos de Datos (JSON, CSV, Parquet)
Justificación:

JSON: Para datos semi-estructurados (redes sociales, logs)

CSV: Para datos tabulares simples (ventas, reportes)

Parquet: Para almacenamiento eficiente y consultas rápidas (datos de IoT)

## 📁 Estructura del Proyecto

```
big_data_project/
├── data/                    # Datos de ejemplo
│   ├── sales.csv           # Datos estructurados de ventas
│   ├── iot_data.csv    # Datos de sensores IoT (formato columnar)
│   ├── social_media.json   # Datos semi-estructurados de redes sociales
│   └── app_logs.txt        # Logs de aplicaciones (texto no estructurado)
├── src/
│   ├── lesson_1/           # Conceptos de Big Data
│   ├── lesson_2/           # Arquitectura de Spark
│   ├── lesson_3/           # Operaciones con RDDs
│   ├── lesson_4/           # Spark SQL y DataFrames
│   ├── lesson_5/           # Spark Streaming
│   └── lesson_6/           # MLlib - Machine Learning
├── config/                 # Configuración de Spark
├── models/                 # Modelos de ML entrenados
├── output/                 # Resultados de procesamiento
└── README.md
```
##  Lecciones Implementadas
### Lección 1: Big Data
**Big Data**: Describe las 5Vs y el ecosistema.
Conceptos: 5V's del Big Data (Volumen, Velocidad, Variedad, Veracidad, Valor)
Tecnologías: Explicación del ecosistema Hadoop/Spark

#### Lección 2: Arquitectura de Spark
**Apache Spark**: Arquitectura y componentes.
Componentes: Driver, Executors, Cluster Manager
Módulos: Spark Core, Spark SQL, Spark Streaming, MLlib

### Lección 3: Procesamiento con RDDs
**RDDs**: Transformaciones y acciones.
#### Operaciones:
Transformaciones: filter(), map(), flatMap(), union(), distinct(), sortBy()
Acciones: collect(), count(), take(), mean(), stdev()

### Lección 4: Spark SQL y DataFrames
**Spark SQL**: DataFrames y consultas optimizadas
#### Funcionalidades:
Creación de DataFrames desde múltiples formatos
Consultas SQL optimizadas
Funciones definidas por usuario (UDFs)
Comparación de rendimiento RDD vs DataFrame

### Lección 5: Spark Streaming
**Spark Streaming**: Procesamiento en tiempo real. Streaming requiere ejecución por separado.
#### Procesamiento en tiempo real:
Conexión con sockets TCP (netcat)
Procesamiento de flujos continuos de datos
Agregaciones en ventanas temporales
Se agrega un test de prueba de streaming antes de ejecutar lección 5 o main opción 2.

### Lección 6: Machine Learning con MLlib
**MLlib**: Machine Learning escalable.
#### Algoritmos implementados:
Regresión logística para clasificación binaria
Preparación de datos y feature engineering
Evaluación de modelos (métricas AUC)
Entrenamiento y predicción distribuida

## Ejecución

1. Instalar dependencias: `pip install -r requirements.txt`
2. Ejecutar el pipeline completo: `python main.py` (antes de se debe ejecutar config/spark_config.py)
3. Probar funcionamientos: ejecutar antes del main.py, spark_test.py, test_python.py, test_spark.py

Nota: La Lección 5 (Streaming) requiere un servidor socket. Puedes probarlo con:
```bash
nc -lk 9999
```
## Instrucciones de Ejecución

1. Instala las dependencias: `pip install -r requirements.txt`
2. Ejecuta el script de configuración de spark: `spark_config.py`
3. Ejecuta en WSL Ubuntu, y déjalo abierto durante el proceso: nc -lk 9999 
4. Ejecuta el script principal: `python main.py`
5. Para probar el streaming (Lección 5), abre una terminal y ejecuta: `nc -lk 9999`
   - Luego ejecuta el script de streaming: `python src/lesson_5/spark_streaming.py`
   - Escribe mensajes en la terminal del netcat para ver el procesamiento en tiempo real

### ⚠️ Nota Importante sobre Compatibilidad en Windows
**Error conocido**: HADOOP_HOME and hadoop.home.dir are unset

Este error aparece al intentar guardar modelos de MLlib en Windows debido a la falta de utilidades de Hadoop. No afecta la funcionalidad del proyecto:

✅ El entrenamiento de modelos funciona correctamente

✅ Las predicciones se realizan sin problemas

✅ El error solo afecta el guardado persistente del modelo

✅ En entornos Linux/cloud, este error no ocurre

**Solución alternativa**: En entornos productivos, se recomienda usar:
Linux o sistemas cloud (Databricks, EMR, HDInsight)

Configurar winutils.exe para Windows (opcional)

## 📊 Uso de los Archivos de Datos
Los archivos en la carpeta data/ son ejemplos que puedes usar para extender el proyecto: Se puede ejecutar `generete_sample_data.py` sino aparece la data instalada.
- **sales.csv**
- **social_media.json**
- **app_logs.txt**
- **iot_data.csv**: Datos de sensores en formato columnar para procesamiento eficiente.

## 🎯 Resultados Obtenidos:
**Rendimiento**: DataFrames 2x más rápidos que RDDs en consultas

**Precisión**: Modelo de ML con AUC 1.0 en datos de prueba

**Escalabilidad**: Arquitectura distribuida para grandes volúmenes

**Tiempo real**: Procesamiento de streaming con latencia mínima

## 📈 Próximos Pasos
Para llevar este proyecto a un entorno productivo:

**Despliegue en cluster**: Configurar Spark en un cluster Hadoop/YARN/Kubernetes

**Orquestación**: Implementar Airflow o Azure Data Factory para pipelines

**Monitoring**: Agregar herramientas de monitoreo (Spark UI, Prometheus)

**Optimización**: Tuning de parámetros de Spark para mejor rendimiento

**CI/CD**: Implementar pipelines de integración continua

## 👥 Autor
By Catalina Millán Coronado.

*Este proyecto completo cubre todos los requerimientos y lecciones solicitadas, proporcionando una base sólida para el procesamiento de big data con Apache Spark.*