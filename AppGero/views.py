from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from AppGero.forms import ArticuloForm
from AppGero.models import Articulo, Tutorial
from .forms import UserRegistrationForm, UserProfileForm, PreguntaForm, RespuestaForm
from django.contrib import messages
from .models import Pregunta, Respuesta, Articulo, UserProfile
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'appgero/index.html')

def articulo(request):
    return render(request, 'appgero/articulo.html')

def herramienta(request):
    return render(request, 'appgero/herramienta.html')

def tutorial(request):
    return render (request, 'appgero/tutorial.html')

def padre(request):
    return render(request, 'appgero/padre.html')

def login(request):
    return render (request, 'appgero/login.html')




@login_required
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'AppGero/profile.html', {'form': form, 'user_profile': user_profile})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('profile')  # Redirige al perfil del usuario
    else:
        form = UserRegistrationForm()
    return render(request, 'Appgero/register.html', {'form': form})

def agregar_tutorial(request):
    if request.method == "POST":  # Si se envió el formulario
        tutorial = Tutorial(titulo=request.POST["titulo"],
        descripcion=request.POST["descripcion"],
        contenido=request.POST["contenido"],
        fecha_publicacion=request.POST["fecha_publicacion"])

        tutorial.save()  # Guarda el artículo en la base de datos
        
        return redirect('inicio')  # Redirige a la página de inicio o a otra vista específica
    
    return render(request, "appgero/agregar_tutorial.html")


@login_required
def agregar_articulo(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user  # Asigna el autor como el usuario actual
            articulo.save()  # Guarda el artículo
            return redirect('inicio')  # Redirige a la página de inicio o a otra vista específica
    else:
        form = ArticuloForm()

    return render(request, "appgero/agregar_articulo.html", {"form": form})



def leerArticulos(request):
    articulos = Articulo.objects.all()  # Recupera todos los artículos
    contexto = {"articulos": articulos}
    return render(request, "appgero/articulo.html", contexto)  # Usamos articulo.html

def detalleArticulo(request, id):
    articulo = Articulo.objects.get(id=id)  # Obtiene un artículo específico por ID
    return render(request, "appgero/leerArticulos.html", {'articulo': articulo})  # Usamos leerArticulo.htmlp

def leerTutoriales(request):
    tutoriales = Tutorial.objects.all()  # Recupera todos los tutoriales
    contexto = {"tutoriales": tutoriales}
    return render(request, "appgero/tutorial.html", contexto)  # Usamos tutorial.html

def detalleTutorial(request, id):
    tutorial = Tutorial.objects.get(id=id)  # Obtiene un tutorial específico por ID
    return render(request, "appgero/leerTutoriales.html", {'tutorial': tutorial})  # Usamos leerTutoriales.html

def lista_tutoriales(request):
    q = request.GET.get('q', '')  # Obtener el valor de búsqueda
    if q:  # Si hay un valor de búsqueda
        # Filtrar tutoriales que contengan la búsqueda en el título o descripción
        tutoriales = Tutorial.objects.filter(titulo__icontains=q) | Tutorial.objects.filter(descripcion__icontains=q)
    else:
        tutoriales = Tutorial.objects.all()  # Si no hay búsqueda, mostrar todos los tutoriales

    return render(request, 'appgero/tutorial.html', {'tutoriales': tutoriales})

def comunidad(request):
    preguntas = Pregunta.objects.all().order_by('-fecha_creacion')  # Obtener todas las preguntas
    return render(request, 'appgero/comunidad.html', {'preguntas': preguntas})

def detalle_pregunta(request, id):
    pregunta = get_object_or_404(Pregunta, id=id)
    respuestas = pregunta.respuestas.all().order_by('-fecha_creacion')  # Carga las respuestas ordenadas por fecha
    form = RespuestaForm()  # Crea una instancia del formulario para respuestas

    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.pregunta = pregunta  # Asigna la pregunta a la respuesta
            respuesta.autor = request.user  # Asigna el autor
            respuesta.save()  # Guarda la respuesta
            return redirect('detalle_pregunta', id=pregunta.id)  # Redirige a la misma pregunta

    return render(request, 'appgero/detalle_pregunta.html', {
        'pregunta': pregunta,
        'respuestas': respuestas,
        'form': form,
    })

def crear_pregunta(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.autor = request.user  # Asigna el autor
            pregunta.save()  # Guarda la pregunta en la base de datos
            messages.success(request, 'Pregunta creada con éxito.')
            return redirect('comunidad')  # Redirige a la vista de comunidad
    else:
        form = PreguntaForm()  # Crea un nuevo formulario vacío
    return render(request, 'appgero/crear_pregunta.html', {'form': form})

def responder_pregunta(request, pregunta_id):
    pregunta = Pregunta.objects.get(id=pregunta_id)
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.pregunta = pregunta
            respuesta.autor = request.user
            respuesta.save()
            messages.success(request, 'Respuesta creada con éxito.')
            return redirect('appgero/comunidad')
    else:
        form = RespuestaForm()
    return render(request, 'appgero/responder_pregunta.html', {'form': form, 'pregunta': pregunta})