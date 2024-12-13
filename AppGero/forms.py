from django import forms
from .models import Tutorial, Pregunta, Respuesta, UserProfile, Articulo
from django.contrib.auth.models import User
from django.db import models

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'nombre', 'apellido']


class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['titulo', 'contenido']

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['contenido']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        # Verificar si las contraseñas coinciden
        if password != password_confirm:
            self.add_error('password_confirm', "Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Establece la contraseña en el modelo
        if commit:
            user.save()
        return user


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'autor', 'imagen']



class TutorialForm(forms.ModelForm):
    class Meta:
        model: Tutorial
        fields = ['titulo', 'descripcion', 'contenido', 'fecha_publicacion']
