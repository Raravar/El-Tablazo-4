from django.urls import path
from .views import form_proveedores,home, contacto, about, dulce, salada, mixta, form_mod_proveedor, form_del_proveedor, listado

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('about', about, name="about"),
    path('dulce', dulce, name="dulce"),
    path('salada', salada, name="salada"),
    path('mixta', mixta, name="mixta"),
    path('form-proveedor', form_proveedores, name="form_proveedor"),
    path('form-mod-proveedor/<id>', form_mod_proveedor, name="form_mod_proveedor"),
    path('form-del-proveedor/<id>', form_del_proveedor, name="form_del_proveedor"),
    path('listado', listado, name="listado"),

]