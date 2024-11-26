from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'appgero/index.html')

def usuario(request):
    return render(request, 'appgero/usuario.html')

def articulo(request):
    return render(request, 'appgero/articulo.html')

def herramienta(request):
    return render(request, 'appgero/herramienta.html')