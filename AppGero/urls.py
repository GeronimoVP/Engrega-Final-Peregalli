from django.urls import path
from AppGero import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('articulo/', views.articulo, name='articulo'),
    path('herramienta/', views.herramienta, name='herramienta'),
    path('usuario/', views.usuario, name='usuario'),
]
