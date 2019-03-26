from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from vehiculos.models import Modelo, Tipo


class Propietario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    numero_documento = models.CharField(max_length=15, verbose_name="número de documento", unique=True)
    soporte_documento = models.FileField(upload_to="propietarios/",
                                         help_text="Cargue el soporte de su documento en: PDF, JPG o PNG",
                                         validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png'])])
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False, verbose_name="fecha de nacimiento")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{CEDULA} - {NOMBRES} {APELLIDOS}".format(CEDULA=self.numero_documento, NOMBRES=self.nombres,
                                                         APELLIDOS=self.apellidos)


class VehiculoPropietario(models.Model):
    class Meta:
        verbose_name = "Vehiculo del propietario"
        verbose_name_plural = "Vehiculos del propietario"

    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='vehiculos')
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    placa = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.modelo.nombre
