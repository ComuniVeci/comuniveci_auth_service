import os
from dotenv import load_dotenv

load_dotenv()

# Variables comunes
TESTING = os.getenv("TESTING")
# Definir nombre de la base de datos según el entorno
if TESTING == "true":
    DB_NAME = os.getenv("DB_NAME_TEST")
else:
    DB_NAME = os.getenv("DB_NAME")
if not DB_NAME:
    raise ValueError("DB_NAME no está definido en el archivo .env")

MONGO_URI = os.getenv("MONGO_URI")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


# Validación obligatoria
if not MONGO_URI:
    raise ValueError("MONGO_URI no está definido en el archivo .env")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY no está definido en el archivo .env")
if not ALGORITHM:
    raise ValueError("ALGORITHM no está definido en el archivo .env")
if not ACCESS_TOKEN_EXPIRE_MINUTES:
    raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES no está definido en el archivo .env")

# Convertir tiempo de expiración a entero
ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES)