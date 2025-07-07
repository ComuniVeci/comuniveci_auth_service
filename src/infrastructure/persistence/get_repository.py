from src.infrastructure.persistence.db import get_db
from src.infrastructure.persistence.mongo_repository import MongoUserRepository

def get_user_repository():
    db = get_db()
    return MongoUserRepository(db)
