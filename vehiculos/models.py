from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Modelo(models.Model):
    class Meta:
        unique_together = 'marca', 'nombre'

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "{modelo} - {marca}".format(modelo=self.nombre, marca=self.marca.nombre)


class Tipo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
