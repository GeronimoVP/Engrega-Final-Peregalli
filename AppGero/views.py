from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppGero.forms import UsuarioForm, ArticuloForm, HerramientaForm
from AppGero.models import Usuario, Articulo, Herramienta

def inicio(request):
    return render(request, 'appgero/index.html')

def usuario(request):
    return render(request, 'appgero/usuario.html')

def articulo(request):
    return render(request, 'appgero/articulo.html')

def herramienta(request):
    return render(request, 'appgero/herramienta.html')


def agregar_usuario(request):
    if request.method == "POST":  # Si se envió el formulario
        usuario = Usuario(nombre=request.POST['nombre'],
        correo=request.POST['correo'],
        contrasenia=request.POST['contrasenia'],
        rol=request.POST['rol'])

        usuario.save()  # Guarda el usuario en la base de datos

        return redirect('inicio')  # Redirige a la página de inicio o a otra vista específica

    return render(request, "appgero/agregar_usuario.html")



def agregar_articulo(request):
    if request.method == "POST":  # Si se envió el formulario
        print("entra1")
        articulo = Articulo(titulo=request.POST["titulo"],
        contenido=request.POST["contenido"],
        autor=request.POST["autor"])
        print ("entra2")  # Crea un objeto Articulo

        articulo.save()  # Guarda el artículo en la base de datos
        
        return redirect('inicio')  # Redirige a la página de inicio o a otra vista específica
    
    return render(request, "appgero/agregar_articulo.html")


def agregar_herramienta(request):
    if request.method == "POST":
        herramienta = Herramienta(nombre=request.POST ["nombre"],
        descripcion=request.POST["descripcion"],
        url=request.POST["url"])

        herramienta.save()

        return redirect('inicio')

    return render(request, 'appgero/agregar_herramienta.html')