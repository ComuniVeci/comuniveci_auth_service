from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter

def setup_metrics(app):
    instrumentator = Instrumentator(
        should_group_status_codes=False,
        should_ignore_untemplated=True,
        should_respect_env_var=False,
        excluded_handlers=["/metrics", "/docs", "/openapi.json"],
        should_instrument_requests_inprogress=True,
    )
    instrumentator.instrument(app).expose(app)

# MÉTRICAS PERSONALIZADAS

login_success_total = Counter(
    "auth_login_success_total", "Total de logins exitosos"
)

login_failure_total = Counter(
    "auth_login_failure_total", "Total de logins fallidos"
)

register_success_total = Counter(
    "auth_register_success_total", "Total de registros exitosos"
)

register_failure_total = Counter(
    "auth_register_failure_total", "Total de errores al registrar"
)

me_requests_total = Counter(
    "auth_me_requests_total", "Total de solicitudes al endpoint /me"
)