from django.db import models

# Create your models here.
class Mascota(models.Model):
    # creo los campos de la clase mascota.
    nombre = models.CharField(max_length=40)
    tamaño = models.CharField(max_length=40)
    raza = models.CharField(max_length=60)

class Entrenador(models.Model):
    
    nombre = models.CharField(max_length=35, default='Sin Nombre')
    edad = models.IntegerField()

class Entrenamiento(models.Model):

    curso = models.CharField(max_length=60)
    