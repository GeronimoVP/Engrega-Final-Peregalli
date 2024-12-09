from django.contrib import admin
from .models import Usuario, Articulo, Herramienta, Tutorial

admin.site.register(Usuario)
admin.site.register(Articulo)
admin.site.register(Herramienta)
admin.site.register(Tutorial)
