from django import forms
from .models import Articulo, Herramienta, Tutorial

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'autor']

class HerramientaForm(forms.ModelForm):
    class Meta:
        model = Herramienta
        fields = ['nombre', 'descripcion', 'url']


class TutorialForm(forms.ModelForm):
    class Meta:
        model: Tutorial
        fields = ['titulo', 'descripcion', 'contenido', 'fecha_publicacion']
