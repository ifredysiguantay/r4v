
# Documentación Técnica - MVP Inmobiliario

## 📐 Arquitectura

- **Framework:** Django,Django REST framework
- **Apps:**
  - `property_catalog`: Gestión y despliegue de propiedades desde la API externa.
  - `appointments`: Agendamiento, modificación y cancelación de citas.
  - `api`: Enrutamiento central y funciones auxiliares.
- **Frontend:** HTML + Tailwind, Charts.js
- **Base de datos:** Postgresql 
- **API externa:** Lectura de propiedades desde `https://test.controldepropiedades.com/api/propiedades/miraiz` (API-KEY requerida)

## ✅ Requerimientos funcionales implementados

- Catálogo de propiedades con imágenes y detalles clave.
- Sistema de citas con crear/modificar/cancelar.
- Formulario de consultas sobre propiedades.
- Panel básico con métricas de estado de citas.
- Diseño responsivo adaptado a móviles y escritorio.

## 🔒 Requerimientos no funcionales

- Autenticación básica (correo y contraseña).
- Validación de entradas en formularios.
- Respuesta ágil (objetivo <2s).

## 🧠 Funcionalidades adicionales propuestas

- Filtro por tipo de propiedad y ubicación.
- Integración con Google Calendar o email para confirmaciones.

## 📊 Manejo de datos

- **Consumo de API:** vía `requests` con header `API-KEY`.
- **Almacenamiento local:** citas y consultas almacenadas en modelos locales.
- **Imágenes:** las URLs se muestran directamente desde la API.
- **Modelo simplificado para propiedades:** mapeo local opcional para permitir búsquedas avanzadas.
- **Seguridad:** headers y validación básica; se recomienda usar HTTPS en producción.

## ⚠️ Limitaciones actuales del MVP

- Sin búsqueda avanzada ni filtrado geográfico.
- Notificaciones limitadas (no hay email/SMS).
- Análisis limitado a conteo básico de estados.
- Imágenes renderizadas sin pre-cache..

## 🧩 Admin personalizado

- List display adaptado por modelo (e.g., citas con fecha, estado y usuario).
- Búsqueda y filtros aplicados en `Property`, `Appointments`, `Consultas`.
- Uso de `ModelAdmin`, `list_display`, `list_filter`, `search_fields`.

---

## 📝 Notas finales

Este MVP cumple con los requerimientos funcionales del assessment y está listo para futuras extensiones, tales como pagos en línea, integración con CRM o generación de leads automatizados.

