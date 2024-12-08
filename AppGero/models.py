from django.db import models
from django.contrib.auth.views import LoginView

# Modelo para Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}, {self.correo}, {self.contrasenia}, {self.rol}"


# Modelo para Articulo
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo}, {self.contenido}, {self.autor}"


# Modelo para Herramienta
class Herramienta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}, {self.descripcion}, {self.url}"


class CustomLoginView(LoginView):
    iniciar_sesion = 'appgero/login.html'  # Asegúrate de tener esta plantilla
    redirect_authenticated_user = True  # Redirige si el usuario ya está autenticado
