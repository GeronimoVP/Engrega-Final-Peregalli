from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppGero/', include('AppGero.urls')),
    path('inicio/', views.inicio, name='inicio'),
    path('usuario/', views.usuario, name='usuario'),
    path('articulo/', views.articulo, name='articulo'),
    path('herramienta/', views.herramienta, name='herramienta'),
    ]