# 🔐 ComuniVeci – Auth Service
Este microservicio se encarga de la autenticación y gestión básica de usuarios para el sistema ComuniVeci. Provee funcionalidades para:

- Registro de nuevos usuarios

- Inicio de sesión y generación de token JWT

- Verificación de sesión y rol (usuario/admin)

- Tokens seguros y expirables

- Protección de rutas con autenticación

- Documentación Swagger automática

- Exposición de métricas Prometheus para monitoreo
---

# ⚙️ Requisitos

- Python 3.10+

- MongoDB en local (puerto 27017 por defecto)

- poetry para gestión del entorno virtual

---

# 🚀 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/ComuniVeci/comuniveci_auth_service
comuniveci_auth_service
```

2. Instala dependencias:

```bash
poetry install
```

3. Crea un archivo .env en la raíz del proyecto con el siguiente contenido:

```env
MONGO_URI=mongodb://localhost:27017/
DB_NAME=authdb
DB_NAME_TEST=communiveci_test
TESTING=false

SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Puedes cambiar el valor de SECRET_KEY por uno más seguro.

---

# ▶️ Ejecución local

Inicia el servidor con:

```bash
poetry run uvicorn src.main:app --reload --port 8002
```

- El servicio estará disponible en: http://localhost:8002

- Documentación Swagger: http://localhost:8002/docs

- Métricas: http://localhost:8002/metrics

---

# 🔄 Endpoints disponibles

Todos los endpoints están bajo el prefijo /api/auth

### 1. POST /api/auth/register

Registra un nuevo usuario.

- Body (JSON):

```json
{
  "email": "usuario@ejemplo.com",
  "username": "usuario1",
  "password": "contraseñaSegura123"
}
```

- Respuesta:

```json
{
  "message": "Usuario registrado correctamente",
  "access_token": "jwt.token.aqui",
  "token_type": "bearer"
}
```

### 2. POST /api/auth/login

Inicia sesión con correo y contraseña válidos.

- Body (JSON):

```json
{
  "email": "usuario@ejemplo.com",
  "password": "contraseñaSegura123"
}
```

- Respuesta:

```json
{
  "access_token": "jwt.token.aqui",
  "token_type": "bearer"
}
```

### 3. GET /api/auth/me

Devuelve los datos del usuario autenticado. Requiere token Bearer en el header.

- Headers:

```json
Authorization: Bearer <token>
```

- Respuesta:

```json
{
  "id": "60abc123...",
  "username": "usuario1",
  "email": "usuario@ejemplo.com",
  "is_admin": false
}
```

---

# 🧪 Tests

Este servicio incluye tests de integración en el repositorio comuniveci_tests. Para ejecutarlos:

Desde la raíz del proyecto de tests:

```bash
poetry run pytest -v --json-report --json-report-file=report.json
poetry run python generate_report.py
```
___IMPORTANTE:___ Es mejor cambiar la variable de entorno TESTS para realizar las pruebas en otra base de datos

```bash
TESTING=true
```

El reporte PDF se genera como TestReport.pdf

---

# 📊 Métricas Prometheus

Este microservicio expone métricas en /metrics para monitoreo y observabilidad. Se utiliza el middleware prometheus-fastapi-instrumentator.

Endpoint:

http://localhost:8002/metrics

Métricas incluidas:

- http_requests_total: número total de solicitudes por endpoint, método y código de estado.

- http_request_duration_seconds: duración de solicitudes por endpoint y método.

- http_request_size_bytes: tamaño de las solicitudes entrantes.

- http_response_size_bytes: tamaño de las respuestas enviadas.

- http_requests_inprogress: cantidad de peticiones en curso.

- http_request_duration_highr_seconds: histograma de latencia detallado (sin etiquetas por endpoint).

- python_gc_*: métricas internas del recolector de basura de Python.

- python_info: información de versión e implementación del entorno Python.

Estas métricas permiten integrar el servicio con sistemas como Prometheus y Grafana para monitoreo y alertas. (Aún no implementado).

---

# 🛡️ Seguridad y tokens

- Los tokens JWT son firmados con el algoritmo HS256

- Contienen el ID del usuario y si es administrador (is_admin)

- Su duración se define con ACCESS_TOKEN_EXPIRE_MINUTES (por defecto 30 minutos)

- Los tokens no se almacenan en base de datos, su validez se verifica al decodificarlos