# logs.py

import logging
import os

# Crear la carpeta de registros
os.makedirs("logs", exist_ok=True)

# Configurar el archivo de registro
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Registrar eventos importantes
def registrar_evento(mensaje):
    logging.info(mensaje)


# Registrar errores del sistema
def registrar_error(mensaje):
    logging.error(mensaje)
