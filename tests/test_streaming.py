import time
import socket


def test_streaming_enhanced():
    """Envía datos de prueba al socket para probar el streaming"""
    print("Conectando al puerto 9999 para enviar datos de prueba...")
    print("Presiona Ctrl+C para detener")

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 9999))

        test_messages = [
            "Hola mundo de Spark Streaming",
            "Big Data es fascinante con Apache Spark",
            "Procesamiento en tiempo real con Python",
            "Streaming de datos con PySpark",
            "Análisis de datos en tiempo real",
            "Machine Learning con datos en streaming"
        ]

        message_count = 0
        while True:
            for message in test_messages:
                full_message = f"{message} - Mensaje #{message_count}\n"
                client_socket.send(full_message.encode('utf-8'))
                print(f"Enviado: {full_message.strip()}")
                message_count += 1
                time.sleep(2)  # Esperar 2 segundos entre mensajes

    except KeyboardInterrupt:
        print("\nDeteniendo envío de datos...")
    except ConnectionRefusedError:
        print("Error: No se pudo conectar al puerto 9999.")
        print("Asegúrate de que el streaming de Spark esté ejecutándose.")
    except Exception as e:
        print(f"Error de conexión: {e}")
    finally:
        try:
            client_socket.close()
        except:
            pass


if __name__ == "__main__":
    test_streaming_enhanced()