from src.domain.entities import User
from src.utils import hash_password


def register_user(user_data, repository):
    existing_user = repository.find_by_email(user_data["email"])
    if existing_user:
        raise ValueError("El correo ya está registrado")

    hashed_password = hash_password(user_data["password"])
    user = User(user_data["email"], user_data["username"], hashed_password)

    return repository.create({
        "email": user.email,
        "username": user.username,
        "hashed_password": user.hashed_password,
        "created_at": user.created_at
    })
