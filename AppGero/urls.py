from django.urls import path
from AppGero import views

urlpatterns = [
    path('AppGero/inicio/', views.inicio, name='inicio' ),
    path('AppGero/articulo/', views.articulo, name='articulo'),
    path('AppGero/herramienta/', views.herramienta, name='herramienta'),
    path('AppGero/usuario/', views.usuario, name='usuario'),
    path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),
    path('agregar_articulo/', views.agregar_articulo, name='agregar_articulo'),
    path('agregar_herramienta/', views.agregar_herramienta, name='agregar_herramienta'),
    path('buscar_usuario/', views.buscar_usuario, name='buscar_usuario'),
]
