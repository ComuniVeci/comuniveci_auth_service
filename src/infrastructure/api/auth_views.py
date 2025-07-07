from fastapi import APIRouter, HTTPException, status
from src.domain.schemas import UserCreateSchema
from src.infrastructure.persistence.get_repository import get_user_repository
from src.usecases.register_user import register_user

auth_router = APIRouter()

@auth_router.get("/ping")
def ping():
    return {"message": "Auth Service is running"}

@auth_router.post("/register", status_code=201)
def register(user: UserCreateSchema):
    repository = get_user_repository()
    try:
        new_user = register_user(user.model_dump(), repository)
        return {"message": "Usuario registrado correctamente", "user_id": new_user["_id"]}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
