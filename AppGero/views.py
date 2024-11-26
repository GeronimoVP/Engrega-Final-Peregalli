from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def usuario(request):
    return render(request, 'usuario.html')

def articulo(request):
    return render(request, 'articulo.html')

def herramienta(request):
    return render(request, 'herramienta.html')