# 📜 CHANGELOG – ComuniVeci Auth Service

Historial de cambios para el microservicio de autenticación en ComuniVeci.

---

## [1.0.0] – 2025-07-10

### 🚀 Funcionalidad inicial completa:

- ✅ Registro de usuarios (/api/auth/register)

    - Hash automático de contraseñas con bcrypt

    - Verificación de correo existente

    - Retorno inmediato de token JWT tras registro

- 🔐 Inicio de sesión (/api/auth/login)

    - Validación de credenciales

    - Generación de token JWT con campo is_admin

- 👤 Endpoint protegido para obtener datos del usuario actual (/api/auth/me)

    - Decodifica y valida el token

    - Devuelve ID, username, email y rol (admin o no)

- 🔧 Configuración por entorno con variables .env

    - Soporte para base de datos de test (TESTING=true)

- 📄 Documentación Swagger (/docs) integrada con FastAPI

- 🧪 Tests de integración desde repositorio comuniveci_tests

    - Incluye generación de reporte en PDF

- 🔒 Mejores prácticas de seguridad:

    - JWT expirables

    - Validaciones robustas con Pydantic

    - Contraseñas hasheadas