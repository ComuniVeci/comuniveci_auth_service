from src.utils import verify_password, create_access_token
from src.domain.repositories import UserRepositoryInterface
from src.infrastructure.metrics import login_success_total, login_failure_total

def login_user(credentials: dict, repository: UserRepositoryInterface):
    user = repository.find_by_email(credentials["email"])
    if not user or not verify_password(credentials["password"], user["hashed_password"]):
        login_failure_total.inc()
        raise ValueError("Credenciales inválidas")
    login_success_total.inc()
    token = create_access_token({
        "sub": str(user["_id"]),
        "is_admin": user.get("is_admin", False)
    })
    return {"access_token": token, "token_type": "bearer"}