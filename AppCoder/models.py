from django.db import models

# Create your models here.
class Cursos(models.Model):
    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()


class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class Entregas(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()

class CursoFormulario(models.Model):
    cursos = models.CharField(max_length=30)
    camada = models.IntegerField()    