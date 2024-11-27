from django import forms
from .models import Usuario, Articulo, Herramienta

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'contrasenia', 'rol']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'autor']

class HerramientaForm(forms.ModelForm):
    class Meta:
        model = Herramienta
        fields = ['nombre', 'descripcion', 'url']


class BuscarUsuarioFormulario(forms.Form):
    criterio = forms.CharField(label='Buscar usuario por nombre o correo', max_length=100, required=True)
