import json
import csv
from datetime import datetime, timedelta
import random
import os

# Crear la carpeta 'data' si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# 1. Generar datos de ventas (sales.csv)
num_sales = 1000
products = [101, 102, 103, 104, 105]

with open('data/sales.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['transaction_id', 'product_id', 'quantity', 'price', 'timestamp'])

    for i in range(1, num_sales + 1):
        transaction_id = i
        product_id = random.choice(products)
        quantity = random.randint(1, 5)
        price = round(random.uniform(10, 100), 2)
        timestamp = (datetime(2023, 1, 1) + timedelta(minutes=5 * i)).strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([transaction_id, product_id, quantity, price, timestamp])

# 2. Generar datos de redes sociales (social_media.json)
num_posts = 100
users = [f'user{i}' for i in range(1, 11)]
contents = [
    "Hello world!",
    "This is a tweet",
    "Just posted a photo",
    "Check out my blog",
    "Having a great day!",
    "Learning Apache Spark",
    "Big data is fun",
    "Just finished my project",
    "Coffee time!",
    "Lunch time!"
]

with open('data/social_media.json', 'w') as f:
    for i in range(num_posts):
        post = {
            'user_id': random.choice(users),
            'post_id': f'post{i + 1}',
            'content': random.choice(contents),
            'likes': random.randint(0, 100),
            'timestamp': (datetime(2023, 1, 1) + timedelta(minutes=5 * i)).isoformat() + 'Z'
        }
        f.write(json.dumps(post) + '\n')

# 3. Generar datos de sensores IoT (en CSV en lugar de Parquet)
num_readings = 1000
sensors = [f'sensor{i}' for i in range(1, 11)]

with open('data/iot_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['sensor_id', 'timestamp', 'temperature', 'humidity'])

    for i in range(num_readings):
        sensor_id = random.choice(sensors)
        timestamp = (datetime(2023, 1, 1) + timedelta(seconds=10 * i)).strftime('%Y-%m-%d %H:%M:%S')
        temperature = round(random.uniform(20, 30), 1)
        humidity = round(random.uniform(50, 80), 1)
        writer.writerow([sensor_id, timestamp, temperature, humidity])

# 4. Generar logs de aplicaciones (app_logs.txt)
num_logs = 100
log_levels = ['INFO', 'ERROR', 'WARN', 'DEBUG']
messages = [
    'Application started',
    'Failed to connect to database',
    'Connection established',
    'User logged in',
    'User logged out',
    'Data processed successfully',
    'Timeout occurred',
    'Task completed',
    'Invalid input',
    'Server restarted'
]

with open('data/app_logs.txt', 'w') as f:
    for i in range(num_logs):
        log_level = random.choice(log_levels)
        message = random.choice(messages)
        timestamp = (datetime(2023, 1, 1) + timedelta(seconds=10 * i)).strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{log_level}] {timestamp} {message}\n")

print("Datos de ejemplo generados en la carpeta 'data'")