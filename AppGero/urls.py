from django.urls import path
from AppGero import views

urlpatterns = [
    path('AppGero/inicio/', views.inicio, name='inicio' ),
    path('AppGero/articulo/', views.articulo, name='articulo'),
    path('AppGero/herramienta/', views.herramienta, name='herramienta'),
    path('AppGero/usuario/', views.usuario, name='usuario'),
]
