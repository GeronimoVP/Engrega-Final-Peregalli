from django.urls import path
from AppGero import views

urlpatterns = [
    path('AppGero/inicio/', views.inicio, name='inicio' ),
    path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),
    path('agregar_articulo/', views.agregar_articulo, name='agregar_articulo'),
    path('agregar_herramienta/', views.agregar_herramienta, name='agregar_herramienta'),
    path('buscar_usuario/', views.buscar_usuario, name='buscar_usuario'),
    path('leerUsuarios/', views.leerUsuarios, name='leerUsuarios'),
    path('herramientas/', views.leerHerramientas, name='lista_herramientas'),
    path('herramientas/<int:id>/', views.detalleHerramienta, name='detalle_herramienta'),
    path('articulos/', views.leerArticulos, name='lista_articulos'),
    path('articulos/<int:id>/', views.detalleArticulo, name='detalle_articulo'),
    path('tutoriales/', views.leerTutoriales, name='lista_tutoriales'),
    path('tutoriales/<int:id>/', views.detalleTutorial, name='detalle_tutorial'),
    path('agregar_tutorial/', views.agregar_tutorial, name='agregar_tutorial'),
]
