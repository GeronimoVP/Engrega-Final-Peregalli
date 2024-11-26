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
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario')  # Redirige a la página de usuarios
    else:
        form = UsuarioForm()
    return render(request, 'agregar_usuario.html', {'form': form})

def agregar_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulo')  # Redirige a la página de artículos
    else:
        form = ArticuloForm()
    return render(request, 'agregar_articulo.html', {'form': form})

def agregar_herramienta(request):
    if request.method == 'POST':
        form = HerramientaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('herramienta')  # Redirige a la página de herramientas
    else:
        form = HerramientaForm()
    return render(request, 'agregar_herramienta.html', {'form': form})