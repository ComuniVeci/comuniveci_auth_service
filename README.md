# 🔐 ComuniVeci – Auth Service
Este microservicio se encarga de la autenticación, gestión de usuarios y generación de tokens seguros para el sistema distribuido ComuniVeci. Forma parte de una arquitectura basada en microservicios e interactúa con el frontend y otros servicios como admin-service.

---

## 🚀 Funcionalidades principales

- ✅ Registro de nuevos usuarios
- 🔑 Inicio de sesión y generación de token JWT
- 🔍 Verificación de sesión actual (endpoint /me)
- 🧑‍💻 Detección de rol administrador (is_admin)
- 🔐 Tokens seguros, firmados y con expiración
- 📋 Exposición de usuarios registrados sin datos sensibles
- 📈 Métricas Prometheus para monitoreo
- 📄 Documentación Swagger automática

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

| Método | Endpoint  | Descripción                                        |
| ------ | --------- | -------------------------------------------------- |
| POST   | /register | Registra un nuevo usuario                          |
| POST   | /login    | Inicia sesión y genera token JWT                   |
| GET    | /me       | Devuelve datos del usuario autenticado             |
| GET    | /users    | Devuelve lista de usuarios sin exponer contraseñas |

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

#### 4. GET /api/auth/users
Retorna una lista de usuarios (solo id, email, username, is_admin). No requiere autenticación, se usa internamente por admin-service.

---

# 🧪 Tests

Este servicio incluye tests de integración en el repositorio comuniveci_tests. Para ejecutarlos:

Desde la raíz del proyecto de tests:

```bash
poetry run pytest -v --json-report --json-report-file=report.json
poetry run python generate_report.py
```

El reporte PDF se genera como TestReport.pdf

---

# 📊 Métricas Prometheus

Este microservicio expone métricas en /metrics para monitoreo y observabilidad. Se utiliza el middleware prometheus-fastapi-instrumentator.

Endpoint:

http://localhost:8002/metrics

Además de las métricas estándar (tiempos de respuesta, conteos por endpoint, tamaño de payload, etc.), se han agregado métricas personalizadas para observar eventos relevantes del sistema:

Métricas incluidas:

- auth_login_success_total: cantidad total de logins exitosos.

- auth_login_failure_total: cantidad total de intentos de login fallidos.

- auth_register_success_total: cantidad total de registros exitosos.

- auth_register_failure_total: cantidad total de errores al registrar.

- auth_me_requests_total: cantidad total de solicitudes exitosas al endpoint /api/auth/me.

Recomendación: Usa Prometheus para recolectarlas y Grafana para visualizarlas.

---

# 🛡️ Seguridad y tokens

- Los tokens JWT son firmados con el algoritmo HS256

- Contienen el ID del usuario y si es administrador (is_admin)

- Su duración se define con ACCESS_TOKEN_EXPIRE_MINUTES (por defecto 30 minutos)

- Los tokens no se almacenan en base de datos, su validez se verifica al decodificarlos