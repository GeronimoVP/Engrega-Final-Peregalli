from django.urls import path
from AppGero import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('articulo/', views.articulo, name='articulo'),
    path('herramienta/', views.herramienta, name='herramienta'),
    path('usuario/', views.usuario, name='usuario'),
]
