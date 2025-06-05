# Inmuebles El Éxito - MVP

Este proyecto es un Producto Mínimo Viable (MVP) desarrollado con Django para la empresa **Inmuebles El Éxito**. Permite a los usuarios visualizar un catálogo de propiedades, agendar citas para visitas, enviar consultas, y revisar métricas básicas.

## 🚀 Tecnologías utilizadas

- Python 3.12+
- Django 4.x
- Postgresql
- chart.js (via CDN)
- Tailwind 
- Django REST framework
- API REST para listado de propiedades

## 📦 Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd rv4


2. Crea un entorno virtual y actívalo:

    python -m venv venv
    source venv/bin/activate 

3. Instala las dependencias:
    pip install -r requeriments.txt


4. Aplica migraciones

    python manage.py migrate

5. Ejecuta el servidor:
    python manage.py runserver

6. Accede a la aplicación:
    http://127.0.0.1:8000/
    

## 🔐 Superusuario (admin)
Para acceder al panel de administración:

python manage.py createsuperuser