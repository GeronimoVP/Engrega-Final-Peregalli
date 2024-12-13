from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from AppGero.forms import ArticuloForm
from AppGero.models import Articulo, Tutorial
from .forms import UserRegistrationForm, UserProfileForm, PreguntaForm, RespuestaForm, ComentarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Pregunta, Respuesta, Articulo, UserProfile

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

    return render(request, 'AppGero/profile.html', {
        'form': form,
        'user_profile': user_profile,
    })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Guarda el usuario
            form.save()

            # Redirige al usuario a la página de inicio de sesión
            return redirect('login')  # Asegúrate de usar el nombre correcto de la URL para iniciar sesión
    else:
        form = UserRegistrationForm()

    return render(request, 'AppGero/register.html', {'form': form})


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
def crear_articulo(request, id=None):
    if id:
        articulo = get_object_or_404(Articulo, id=id)
    else:
        articulo = None

    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user  # Asigna el usuario actual como autor
            articulo.save()
            return redirect('lista_articulos')  # Redirige a la lista de artículos
    else:
        form = ArticuloForm(instance=articulo)

    return render(request, "appgero/agregar_articulo.html", {"form": form})

@login_required
def eliminar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    if request.method == 'POST':
        articulo.delete()
        return redirect('lista_articulos')  # Redirige a la lista de artículos
    return render(request, 'appgero/eliminar_articulo.html', {'articulo': articulo})

def lista_articulos(request):
    articulos = Articulo.objects.all()  # Recupera todos los artículos
    return render(request, "appgero/lista_articulos.html", {"articulos": articulos})

def detalleArticulo(request, id):
    articulo = Articulo.objects.get(id=id)
    comentarios = articulo.comentarios.all()

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.autor = request.user
            comentario.save()
            return redirect('detalle_articulo', id=articulo.id)
    else:
        form = ComentarioForm()

    return render(request, "appgero/leerArticulos.html", {
        'articulo': articulo,
        'comentarios': comentarios,
        'form': form
    })

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