from django.contrib import admin
from django.urls import path
from app_entrega1.views import *

urlpatterns = [
   path("",inicio,name="inicio"),
   path("productos/",guardar_productos, name='guardar_productos'),
   path("proveedores/",guardar_proveedores, name='guardar_proveedores'),
   path("ventas/",guardar_ventas, name='guardar_ventas'),

   path("buscar_productos/",buscar_productos, name='buscar_productos'),
   path("buscar_proveedores/",buscar_proveedores, name='buscar_proveedores'),
   path("buscar_ventas/",buscar_ventas, name='buscar_ventas'),
   path("eliminar_ventas/<venta_id>",eliminar_ventas, name='eliminar_ventas'),
    path("editar_venta/<venta_id>",editar_venta, name='editar_venta'),
]