from django.urls import path
from AppGero import views

urlpatterns = [
    path('AppGero/inicio/', views.inicio ),
    path('AppGero/articulo/', views.articulo),
    path('AppGero/herramienta/', views.herramienta),
    path('AppGero/usuario/', views.usuario),
]
