from django.db import models
# Create your models here.

#Modelo para Proveedor

class Proveedor(models.Model):
    Identificacion = models.CharField(max_length=9, primary_key=True, verbose_name="Número de identificación")
    Nombre = models.CharField(max_length=50, verbose_name="Nombre completo")
    Telefono = models.CharField(max_length=12, null=True, blank=True, verbose_name="Teléfono")
    Direccion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Dirección")
    Correo = models.CharField(max_length=50, null=True, blank=True, verbose_name="Correo")
    Contraseña = models.CharField(max_length=12, null=True, blank=True, verbose_name="Contraseña")
    Pais = models.CharField(max_length=15, null=True, blank=True, verbose_name="Pais")
    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.Identificacion