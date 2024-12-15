# CyberShield Web Application

## Descripción del Proyecto
CyberShield es una aplicación web desarrollada con Django para proporcionar una plataforma de gestión y visualización de artículos y tutoriales relacionados con la ciberseguridad. Además de contar con un sistema de autenticación de usuarios, esta aplicación permite que los usuarios registrados agreguen, editen y consulten artículos y tutoriales. El proyecto también incluye una comunidad donde los usuarios pueden interactuar, hacer preguntas y compartir conocimientos.

## Requisitos
- Python: 3.8 o superior.
- Django: 5.x
- Base de datos: SQLite (configurada por defecto en el proyecto).

## Dependencias
- plaintext
- asgiref==3.8.1
- Django==5.1.3
- sqlparse==0.5.2
- typing_extensions==4.12.2
- tzdata==2024.2
## Estructura del Proyecto
- AppCyberShield/: Contiene las vistas, modelos y formularios del proyecto.
- templates/: Incluye las páginas HTML del proyecto.
- static/: Archivos CSS para personalización visual.
## Funcionalidades
- Agregar Artículos
URL: /agregar_articulo/
Descripción: Permite registrar artículos con título, contenido y autor.
- Agregar Tutoriales
URL: /agregar_tutorial/
Descripción: Permite registrar tutoriales con título, descripción, autor y un enlace.
- Comunidad
URL: /comunidad/
Descripción: Una sección donde los usuarios pueden ver y participar en discusiones sobre ciberseguridad.
- Búsqueda de Artículos y Tutoriales
URL: /buscar_articulo/
Descripción: Permite a los usuarios buscar artículos y tutoriales registrados en la base de datos.
Autenticación de Usuarios
- Los usuarios pueden registrarse, iniciar sesión y acceder a su perfil.

## Instrucciones de Instalación
- Clonar este repositorio:
git clone https://github.com/tuusuario/cybershield.git
  
- Instalar las dependencias:
pip install -r requirements.txt

- Ejecutar las migraciones de la base de datos:
python manage.py migrate

-Crear un superusuario (opcional, para administración):
python manage.py createsuperuser

- Iniciar el servidor:
python manage.py runserver

- Accede a la aplicación en http://127.0.0.1:8000

## Orden para Probar las Funcionalidades
- Registrar Usuarios: Agregar al menos un usuario en /agregar_usuario/.
- Agregar Artículos y Tutoriales: Publicar artículos y tutoriales en /agregar_articulo/ y /agregar_tutorial/.
- Buscar Artículos y Tutoriales: Utilizar la funcionalidad de búsqueda en /buscar_articulo/ para encontrar artículos o tutoriales específicos.
- Unirse a la Comunidad: Participar en discusiones sobre ciberseguridad a través de /comunidad/.