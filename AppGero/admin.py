from django.contrib import admin
from .models import Articulo, Herramienta, Tutorial

admin.site.register(Articulo)
admin.site.register(Herramienta)
admin.site.register(Tutorial)