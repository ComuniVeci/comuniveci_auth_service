from fastapi import APIRouter, HTTPException, status
from src.domain.schemas import UserCreateSchema, UserLoginSchema
from src.infrastructure.persistence.get_repository import get_user_repository
from src.usecases.register_user import register_user
from src.usecases.login_user import login_user

auth_router = APIRouter()

@auth_router.get("/ping")
def ping():
    return {"message": "Auth Service is running"}

@auth_router.post("/register", status_code=201)
def register(user: UserCreateSchema):
    repository = get_user_repository()
    try:
        new_user = register_user(user.model_dump(), repository)
        return {
            "message": "Usuario registrado correctamente", 
            "user_id": str(new_user["_id"]),
            "username": new_user["username"],
            "email": new_user["email"],
            "is_admin": new_user.get("is_admin", False)
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@auth_router.post("/login")
def login(credentials: UserLoginSchema):
    repository = get_user_repository()
    try:
        return login_user(credentials.model_dump(), repository)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
