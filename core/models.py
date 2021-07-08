from django.db import models
# Create your models here.

#Modelo para Proveedor

class Pais(models.Model):
    idPais = models.IntegerField(primary_key=True, verbose_name="Id de pais")
    nombrePais = models.CharField(max_length=50, verbose_name="Nombre del pais")

    def str(self):
        return self.nombrePais

class Proveedor(models.Model):
    Identificacion = models.CharField(max_length=9, primary_key=True, verbose_name="Número de identificación")
    Nombre = models.CharField(max_length=50, verbose_name="Nombre completo")
    Telefono = models.CharField(max_length=12, null=True, blank=True, verbose_name="Teléfono")
    Direccion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Dirección")
    Correo = models.CharField(max_length=50, null=True, blank=True, verbose_name="Correo")
    Contraseña = models.CharField(max_length=12, null=True, blank=True, verbose_name="Contraseña")
    Pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.Identificacion