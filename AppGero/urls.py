from django.urls import path
from AppGero import views

urlpatterns = [
    path('inicio/', views.inicio ),
    path('articulo/', views.articulo),
    path('herramienta/', views.herramienta),
    path('usuario/', views.usuario),
]
