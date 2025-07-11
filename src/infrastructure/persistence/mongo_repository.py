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
    
    def find_by_id(self, user_id: str) -> dict | None:
        from bson import ObjectId
        return self.collection.find_one({"_id": ObjectId(user_id)})
    
    def find_all(self) -> list[dict]:
        return list(self.collection.find({}, {"password": 0, "hashed_password": 0}))
