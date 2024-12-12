from django.db import models
from django.contrib.auth.models import User

class Pregunta(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='respuestas', on_delete=models.CASCADE)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Respuesta a: {self.pregunta.titulo}'

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
    


class Tutorial(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
