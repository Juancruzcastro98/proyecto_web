from django.shortcuts import render

# Create your views here.

def inicio (request):
    nombre = "Pepe"
    return render (request, "AppCoder/inicio.html", {"name": nombre})


def cursos (request):
    return render(request, "AppCoder/cursos.html")

def entregas (request):
    return render(request, "AppCoder/entregas.html")


def profes (request):
    return render(request, "AppCoder/profes.html")


def estudiantes (request):
    return render(request, "AppCoder/estudiantes.html")