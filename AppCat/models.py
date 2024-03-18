from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    direccion = models.CharField (max_length=100)

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    fecha = models.DateField()
    productos =models.CharField(max_length=500)
    direccion = models.CharField (max_length=100)
    nombreFiesta = models.CharField(max_length=50)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreFiesta
    
class presupuesto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    productos = models.CharField(max_length=500)
    direccion = models.CharField(max_length=100)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)


    def __str__(self) :
        return self.nombre
    
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)