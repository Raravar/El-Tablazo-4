from core.models import Proveedor
from django.contrib import admin
from .models import Proveedor
from .models import Pais

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Pais)