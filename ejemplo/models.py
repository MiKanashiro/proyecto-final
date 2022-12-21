from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    humano = models.CharField(max_length=100)
    
    def __str__(self):
      return f"{self.nombre}, {self.edad}, {self.humano}"
      
class Auto(models.Model):
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    patente = models.CharField(max_length=100)
    
    def __str__(self):
      return f"{self.modelo}, {self.color}, {self.patente}"