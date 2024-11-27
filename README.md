Tercera Pre-entrega: Peregalli

Descripción del Proyecto:
Este proyecto es una aplicación web desarrollada con Django para gestionar usuarios, herramientas, y artículos, además de incluir funcionalidades de búsqueda en la base de datos.

Requisitos
Python: 3.8 o superior.
Django: 4.x
Base de datos SQLite (configurada por defecto en el proyecto).

asgiref==3.8.1
Django==5.1.3
sqlparse==0.5.2
typing_extensions==4.12.2
tzdata==2024.2

Estructura del Proyecto
AppGero/: Contiene las vistas, modelos y formularios del proyecto.
templates/: Incluye las páginas HTML del proyecto.
static/: Archivos CSS para personalización visual.
Funcionalidades

Agregar Usuarios:
URL: /agregar_usuario/
Formulario para registrar usuarios con nombre, correo, contraseña, y rol.

Agregar Herramientas:
URL: /agregar_herramienta/
Permite registrar herramientas con nombre, descripción y URL.

Agregar Artículos:
URL: /agregar_articulo/
Formulario para añadir artículos con título, contenido y autor.

Búsqueda de Usuarios:
URL: /buscar_usuario/
Ingresar un nombre para buscar usuarios registrados en la base de datos.
Orden para Probar las Funcionalidades

Registrar Usuarios:
Agrega al menos un usuario en /agregar_usuario/.

Registrar Herramientas:
Añade herramientas relacionadas a los usuarios en /agregar_herramienta/.

Registrar Artículos:
Publica artículos en /agregar_articulo/.

Buscar Usuarios:
Busca un usuario registrado mediante /buscar_usuario/.
