from django.urls import path
from AppGero import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import lista_tutoriales
from .views import comunidad, crear_pregunta, responder_pregunta, detalle_pregunta

urlpatterns = [
    path('comunidad/', comunidad, name='comunidad'),
    path('comunidad/crear/', crear_pregunta, name='crear_pregunta'),
    path('comunidad/responder/<int:pregunta_id>/', responder_pregunta, name='responder_pregunta'),
    path('pregunta/<int:id>/', detalle_pregunta, name='detalle_pregunta'),  # Asegúrate de que esta línea esté presente
    path('tutoriales/', lista_tutoriales, name='lista_tutoriales'),
    path('AppGero/inicio/', views.inicio, name='inicio' ),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='AppGero/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('articulos/', views.leerArticulos, name='lista_articulos'),
    path('tutoriales/', views.leerTutoriales, name='lista_tutoriales'),
    path('herramientas/', views.leerHerramientas, name='lista_herramientas'),
    path('agregar_tutorial/', views.agregar_tutorial, name='agregar_tutorial'),
    path('agregar_articulo/', views.agregar_articulo, name='agregar_articulo'),
    path('agregar_herramienta/', views.agregar_herramienta, name='agregar_herramienta'),
    path('herramientas/<int:id>/', views.detalleHerramienta, name='detalle_herramienta'),
    path('articulos/<int:id>/', views.detalleArticulo, name='detalle_articulo'),
    path('tutoriales/<int:id>/', views.detalleTutorial, name='detalle_tutorial'),
    ]
