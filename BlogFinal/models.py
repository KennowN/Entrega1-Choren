from django.db import models

class Verduleria(models.Model):
    nombre = models.CharField(max_length=100)
    calle = models.CharField(max_length=50)
    altura = models.IntegerField()
    localidad = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=10)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}- Dirección: {self.calle} {self.altura} "

class Carniceria(models.Model):
    nombre = models.CharField(max_length=100)
    calle = models.CharField(max_length=50)
    altura = models.IntegerField()
    localidad = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=10)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}- Dirección: {self.calle} {self.altura}"

class Panaderia(models.Model):
    nombre = models.CharField(max_length=100)
    calle = models.CharField(max_length=50)
    altura = models.IntegerField()
    localidad = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=10)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}- Dirección: {self.calle} {self.altura}"