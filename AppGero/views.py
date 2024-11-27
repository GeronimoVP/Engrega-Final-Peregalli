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
            usuario =  Usuario(nombre=request.POST['usuario'],correo=request.POST['correo'],contraseña=request.POST['contraseña'],rol=request.POST['rol'])

            usuario.save()  # Guarda el usuario en la base de datos
            return redirect('AppGero/index.html')  # Redirige a la página de inicio o a otra vista específica

    return render(request, "appgero/agregar_usuario.html")



def agregar_articulo(request):
    if request.method == "POST":  # Si se envió el formulario
        miFormulario = ArticuloForm(request.POST)  # Instancia el formulario con los datos enviados
        print(miFormulario)  # Para depuración (opcional)

        if miFormulario.is_valid():  # Verifica si los datos son válidos
            informacion = miFormulario.cleaned_data  # Obtén los datos limpios y validados
            articulo = Articulo(
                titulo=informacion["titulo"],
                contenido=informacion["contenido"],
                autor=informacion["autor"]
            )  # Crea un objeto Articulo
            articulo.save()  # Guarda el artículo en la base de datos
            return redirect('inicio')  # Redirige a la página de inicio o a otra vista específica
    else:
        miFormulario = ArticuloForm()  # Muestra un formulario vacío inicialmente

    return render(request, "appgero/agregar_articulo.html", {"form": miFormulario})


def agregar_herramienta(request):
    return render(request, 'AppGero/agregar_herramienta.html')