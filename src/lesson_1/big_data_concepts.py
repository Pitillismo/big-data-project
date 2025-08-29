def describe_big_data():
    """
    Describe las 5Vs del Big Data y el ecosistema.
    """
    print("Lección 1: Big Data")
    print("=" * 50)

    # Definición de las 5Vs
    five_vs = {
        "Volumen": "Grandes cantidades de datos (terabytes, petabytes).",
        "Velocidad": "Datos que se generan a alta velocidad y requieren procesamiento rápido.",
        "Variedad": "Datos en distintos formatos (estructurados, semi-estructurados, no estructurados).",
        "Veracidad": "Calidad y confiabilidad de los datos.",
        "Valor": "Capacidad de extraer información valiosa para la toma de decisiones."
    }

    print("Las 5Vs del Big Data:")
    for v, description in five_vs.items():
        print(f"- {v}: {description}")

    # Describir el enfoque distribuido
    print("\nBeneficios del enfoque distribuido frente al local:")
    benefits = [
        "Escalabilidad horizontal: Añadir más nodos para manejar más datos.",
        "Tolerancia a fallos: El sistema sigue funcionando aunque falle un nodo.",
        "Procesamiento paralelo: Mayor velocidad al procesar datos en múltiples nodos."
    ]
    for benefit in benefits:
        print(f"- {benefit}")

    # Mapa de tecnologías
    print("\nTecnologías clave en el proyecto:")
    technologies = {
        "Apache Spark": "Motor de procesamiento distribuido para big data.",
        "Hadoop HDFS": "Sistema de archivos distribuido para almacenar grandes volúmenes.",
        "Apache Kafka": "Plataforma de streaming para ingesta de datos en tiempo real.",
        "MLlib": "Biblioteca de machine learning de Spark.",
        "Docker": "Contenedores para empaquetar y ejecutar la aplicación de forma aislada."
    }
    for tech, desc in technologies.items():
        print(f"- {tech}: {desc}")


if __name__ == "__main__":
    describe_big_data()