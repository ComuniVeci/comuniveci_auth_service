from src.utils import verify_password, create_access_token
from src.domain.repositories import UserRepositoryInterface

def login_user(credentials: dict, repository: UserRepositoryInterface):
    user = repository.find_by_email(credentials["email"])
    if not user or not verify_password(credentials["password"], user["hashed_password"]):
        raise ValueError("Credenciales inválidas")
    token = create_access_token({"sub": str(user["_id"])})
    return {"access_token": token, "token_type": "bearer"}