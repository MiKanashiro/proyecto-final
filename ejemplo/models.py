from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.IntegerField()
    
    def __str__(self):
      return f"{self.nombre}, {self.fecha_nacimiento}, {self.id}"
