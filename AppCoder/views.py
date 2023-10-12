from django.shortcuts import render
from .forms import *

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

def cursoFormulario(request):
    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            Cursos = cursos ( request.POST['cursos'], request.POST['camada'])

            cursos.save()

            return render(request, "AppCoder/inicio.html")
    
    else:

        miFormulario= CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})



def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")



def buscar(request):

    respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"

    #return HttpResponse(respuesta)