from prometheus_fastapi_instrumentator import Instrumentator

def setup_metrics(app):
    instrumentator = Instrumentator(
        should_group_status_codes=False,
        should_ignore_untemplated=True,
        should_respect_env_var=True,
        excluded_handlers=["/metrics", "/docs", "/openapi.json"],
        should_instrument_requests_inprogress=True,
    )
    instrumentator.instrument(app).expose(app)