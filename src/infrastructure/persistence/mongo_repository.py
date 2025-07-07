from src.domain.repositories import UserRepositoryInterface
from bson import ObjectId

class MongoUserRepository(UserRepositoryInterface):
    def __init__(self, db):
        self.collection = db["users"]

    def create(self, user_data):
        result = self.collection.insert_one(user_data)
        user_data["_id"] = str(result.inserted_id)
        return user_data

    def find_by_email(self, email):
        return self.collection.find_one({"email": email})
