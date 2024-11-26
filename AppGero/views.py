from django.shortcuts import render

# Vistas principales
def inicio(req):
    return render(req, 'appgero/base.html')

def usuario(req):
    return render(req, 'appgero/usuario.html')

def articulo(req):
    return render(req, 'appgero/articulo.html')

def herramienta(req):
    return render(req, 'appgero/herramienta.html')