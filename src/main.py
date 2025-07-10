from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.infrastructure.api.routes import router as api_router
from src.infrastructure.metrics import setup_metrics

app = FastAPI(
    title="Auth Service - ComuniVeci",
    description="Servicio de autenticación de usuarios para la plataforma ComuniVeci.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # o ["*"] para todos los orígenes (solo en desarrollo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rutas de la API
app.include_router(api_router)

# Configurar métricas
setup_metrics(app)