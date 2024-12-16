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

## LINK VIDEO EXPLICATIVO: 
- https://drive.google.com/file/d/1UZREQTgJbRG-DuzGPEZf9undCQyidssX/view?usp=sharing
## EXCEL CASOS DE PRUEBA:
- https://docs.google.com/spreadsheets/d/1D-KuAFr4Ha1cYhJrL9ge09_UyCD046cd/edit?usp=sharing&ouid=109229044969013523747&rtpof=true&sd=true

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

## USUARIO ADMINISTRADOR KEY:
- user: superadminuser
- pass: 101213gero

  ## PERMISOS

  - Se implementaron permisos por grupo de usuarios en /admin. Un perfil nuevo, sin los permisos necesarios (registrarse) no podra acceder a las opciones de editar, o eliminar articulo.
  - Como prueba de esto aqui hay otro usuario (Moderador) con permisos de edicion:
 
  - user: UsuarioModerador
  - pass: usuariomoderador

## Orden para Probar las Funcionalidades
- Registrar Usuarios: Agregar al usuario en/agregar_usuario/.
- Agregar Artículos, tutoriales y Foro (Q&A entre usuarios): Publicar artículos, tutoriales y participar en el foro en en /agregar_articulo/, /agregar_tutorial/ y /comunidad/crear/.
- Perfiles: Una seccion para personalizar tu perfil, cambiando la foto y editando los detalles personales.
- Buscar Tutoriales: Utilizar la funcionalidad de búsqueda en /tutoriales/ para encontrar tutoriales específicos.
- Unirse a la Comunidad: Participar en discusiones sobre ciberseguridad a través de /comunidad/.

## Objetivo y Vision
-Mi objetivo al crear esta web de ciberseguridad fue dar un paso más allá de los tradicionales tutoriales y artículos estáticos, creando un espacio donde los usuarios no solo aprendieran, sino que también pudieran interactuar, compartir y mejorar juntos. 🌐✨

-La web combina una sección de artículos que ofrece una mirada profunda sobre los últimos retos de la ciberseguridad, abordando desde los conceptos básicos hasta las amenazas más avanzadas que acechan a la sociedad digital actual. 🔍💻

-Pero no quería que solo fuera una plataforma de lectura, sino un espacio donde las personas pudieran aprender activamente. Por eso, añadí una sección de tutoriales prácticos que van más allá de la teoría, guiando a los usuarios paso a paso en la implementación de prácticas de seguridad. 🛡️📚

-Sin importar si eres nuevo en el mundo de la ciberseguridad o si ya eres un experto, cada tutorial está diseñado para ser lo suficientemente accesible, pero también desafiante para fomentar el aprendizaje continuo. 🚀

-Y lo más importante, quise que todo este conocimiento compartido fuera dinámico. No quería que la interacción se limitara a la lectura pasiva, por eso creé un foro interactivo donde la comunidad pueda debatir, preguntar, compartir consejos y soluciones, y aportar su visión sobre el futuro de la seguridad digital. 💬🤝

-Los comentarios en los artículos son otro lugar clave para crear esa conversación, un espacio donde las ideas se pueden enriquecer con diversas perspectivas y experiencias. 💡🌍

-Mi visión es clara: ser una fuente confiable, colaborativa y accesible para todos los que buscan mejorar su conocimiento en ciberseguridad. Ya sea que desees proteger tu privacidad personal, mejorar la seguridad en tu empresa o simplemente aprender a manejar mejor tus dispositivos, esta plataforma está pensada para acompañarte en ese viaje. Y lo mejor de todo, está pensada para hacer que el aprendizaje y la colaboración sean parte de la misma experiencia. 🤗🔐
