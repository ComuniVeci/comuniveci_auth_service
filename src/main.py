from fastapi import FastAPI
from src.infrastructure.api.routes import router as api_router
from src.infrastructure.metrics import setup_metrics

app = FastAPI(
    title="Auth Service - ComuniVeci",
    description="Servicio de autenticación de usuarios para la plataforma ComuniVeci.",
    version="1.0.0"
)

# Registrar rutas de la API
app.include_router(api_router)

# Configurar métricas
setup_metrics(app)