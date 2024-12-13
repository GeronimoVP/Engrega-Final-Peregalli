from django.contrib import admin
from .models import Articulo, Tutorial, Pregunta, Respuesta

admin.site.register(Articulo)
admin.site.register(Tutorial)
admin.site.register(Pregunta)
admin.site.register(Respuesta)