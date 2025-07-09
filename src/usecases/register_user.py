from src.domain.entities import User
from src.utils import hash_password


def register_user(user_data, repository):
    existing_user = repository.find_by_email(user_data["email"])
    if existing_user:
        raise ValueError("El correo ya está registrado")

    hashed_password = hash_password(user_data["password"])
    user = User(
        email=user_data["email"],
        username=user_data["username"], 
        hashed_password=hashed_password,
        is_admin=user_data.get("is_admin", False)
    )

    return repository.create({
        "email": user.email,
        "username": user.username,
        "hashed_password": user.hashed_password,
        "is_admin":user.is_admin,
        "created_at": user.created_at
    })
