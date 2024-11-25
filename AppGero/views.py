from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(req):
    return render(req, 'appgero/index.html')

def cursos(req):
    return render(req, 'appgero/cursos.html')

def profesores(req):
    return HttpResponse(req, 'appgero/profesores.html')

def estudiantes(req):
    return HttpResponse(req, 'appgero/estudiantes.html')

def entregables(req):
    return HttpResponse(req, 'appgero/entregables.html')