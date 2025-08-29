import sys
import os

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"PYSPARK_PYTHON: {os.environ.get('PYSPARK_PYTHON', 'Not set')}")
print(f"PYSPARK_DRIVER_PYTHON: {os.environ.get('PYSPARK_DRIVER_PYTHON', 'Not set')}")