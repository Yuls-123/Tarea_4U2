from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    fundacion = models.IntegerField()
    estadio = models.CharField(max_length=100)
    entrenador = models.CharField(max_length=100)
    capacidad_estadio = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
