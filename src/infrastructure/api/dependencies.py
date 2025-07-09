from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from src.config import SECRET_KEY, ALGORITHM
from src.domain.repositories import UserRepositoryInterface
from src.infrastructure.persistence.get_repository import get_user_repository as get_repo

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_user_repository():
    return get_repo()

def get_current_user(token: str = Depends(oauth2_scheme), repository: UserRepositoryInterface = Depends(get_user_repository)):
    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="No autenticado",
    headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = repository.find_by_id(user_id)
    if user is None:
        raise credentials_exception

    return user