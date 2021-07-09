from django.forms import ModelForm
from .models import Proveedor
from django import forms

class ProveedoresForm(ModelForm):
    Contraseña = forms.CharField(widget=forms.PasswordInput(render_value=True))
    
    class Meta:
        model = Proveedor
        
        fields = ['Identificacion', 'Nombre', 'Telefono', 'Direccion', 'Correo', 'Contraseña', 'Pais']