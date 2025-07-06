from fastapi import APIRouter
from src.infrastructure.api.auth_views import auth_router

router = APIRouter()

# Rutas relacionadas con autenticación
router.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
