from django.db import models

# Modelo para Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Modelo para Articulo
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


# Modelo para Herramienta
class Herramienta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre
