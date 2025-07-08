import os
from pymongo import MongoClient
from src.config import MONGO_URI, DB_NAME

def get_db():
    print(f"[INFO] Conectando a base de datos: {DB_NAME}")
    client = MongoClient(MONGO_URI)
    return client[DB_NAME]
