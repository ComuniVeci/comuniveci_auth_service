from src.domain.repositories import UserRepositoryInterface

def get_all_users(repository: UserRepositoryInterface) -> list[dict]:
    users = repository.find_all()
    return [
        {
            "id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"],
            "is_admin": user.get("is_admin", False)
        }
        for user in users
    ]
