from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('usuario/', views.usuario, name='usuario'),
    path('articulo/', views.articulo, name='articulo'),
    path('herramienta/', views.herramienta, name='herramienta'),
]