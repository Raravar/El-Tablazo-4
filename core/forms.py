from django.forms import ModelForm
from .models import Proveedor

class ProveedoresForm(ModelForm):

    
    class Meta:
        model = Proveedor
        fields = ['Identificacion', 'Nombre', 'Telefono', 'Direccion', 'Correo', 'Contraseña', 'Pais']