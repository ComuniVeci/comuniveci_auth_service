from fastapi import APIRouter, HTTPException, status, Depends
from src.domain.schemas import UserCreateSchema, UserLoginSchema
from src.infrastructure.persistence.get_repository import get_user_repository
from src.usecases.register_user import register_user
from src.usecases.login_user import login_user
from src.utils import create_access_token
from src.infrastructure.api.dependencies import get_current_user

auth_router = APIRouter()

@auth_router.post(
        "/register", 
        status_code=201,
        summary="Registrar nuevo usuario",
        response_description="Usuario registrado correctamente con token de acceso",
        )
def register(user: UserCreateSchema):
    """
    Registra un nuevo usuario con correo, nombre de usuario y contraseña.
    Retorna un token JWT válido para la sesión actual.
    """
    repository = get_user_repository()
    try:
        new_user = register_user(user.model_dump(), repository)
        token = create_access_token({"sub": str(new_user["_id"]), "is_admin": new_user.get("is_admin", False)})
        return {
            "message": "Usuario registrado correctamente", 
            "access_token": token,
            "token_type": "bearer"
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@auth_router.post(
        "/login",
        summary="Iniciar sesión",
        response_description="Token JWT si las credenciales son válidas",
        )
def login(credentials: UserLoginSchema):
    """
    Inicia sesión con correo y contraseña válidos.
    Retorna un token JWT para el usuario autenticado.
    """
    repository = get_user_repository()
    try:
        return login_user(credentials.model_dump(), repository)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

@auth_router.get(
        "/me",
        summary="Obtener información del usuario autenticado",
        response_description="Datos del usuario actual extraídos del token JWT",
        )
def get_profile(current_user: dict = Depends(get_current_user)):
    """
    Devuelve información del usuario autenticado (extraída del token).
    Este endpoint requiere un token válido en el header Authorization.
    """
    return {
        "id": str(current_user["_id"]),
        "username": current_user["username"],
        "email": current_user["email"],
        "is_admin": current_user.get("is_admin", False)
    }
