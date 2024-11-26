from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppGero.forms import UsuarioForm, ArticuloForm, HerramientaForm

def inicio(request):
    return render(request, 'appgero/index.html')

def usuario(request):
    return render(request, 'appgero/usuario.html')

def articulo(request):
    return render(request, 'appgero/articulo.html')

def herramienta(request):
    return render(request, 'appgero/herramienta.html')


def agregar_usuario(request):
    return render(request, 'AppGero/agregar_usuario.html')

def agregar_articulo(request):
    return render(request, 'AppGero/agregar_articulo.html')

def agregar_herramienta(request):
    return render(request, 'AppGero/agregar_herramienta.html')