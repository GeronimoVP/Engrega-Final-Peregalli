from django.urls import path
from AppGero import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import lista_tutoriales
from .views import comunidad, crear_pregunta, responder_pregunta, detalle_pregunta
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('comunidad/', views.comunidad, name='comunidad'),
    path('comunidad/crear/', views.crear_pregunta, name='crear_pregunta'),
    path('comunidad/responder/<int:pregunta_id>/', views.responder_pregunta, name='responder_pregunta'),
    path('pregunta/<int:id>/', views.detalle_pregunta, name='detalle_pregunta'),
    path('tutoriales/', views.lista_tutoriales, name='lista_tutoriales'),
    path('AppGero/inicio/', views.inicio, name='inicio'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='AppGero/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Rutas para Artículos
    path('articulos/', views.lista_articulos, name='lista_articulos'),  # Ruta para listar artículos
    path('articulos/crear/', views.crear_articulo, name='crear_articulo'),  # Ruta para crear un nuevo artículo
    path('articulos/actualizar/<int:id>/', views.crear_articulo, name='actualizar_articulo'),  # Ruta para actualizar un artículo existente
    path('articulos/<int:id>/', views.detalleArticulo, name='detalle_articulo'),  # Ruta para ver el detalle del artículo
    path('articulos/eliminar/<int:id>/', views.eliminar_articulo, name='eliminar_articulo'),  # Ruta para eliminar un artículo
    
    # Rutas para Tutoriales
    path('tutoriales/', views.leerTutoriales, name='lista_tutoriales'),
    path('agregar_tutorial/', views.agregar_tutorial, name='agregar_tutorial'),
    path('tutoriales/<int:id>/', views.detalleTutorial, name='detalle_tutorial'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
