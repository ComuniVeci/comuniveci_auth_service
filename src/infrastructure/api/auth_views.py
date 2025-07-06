from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.get("/ping")
def ping():
    return {"message": "Auth Service is running"}
