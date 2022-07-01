from django.contrib import admin
from .models import DetalleVenta, Producto,Personas, Venta
# Register your models here.

admin.site.register(Producto)
admin.site.register(Personas)
admin.site.register(Venta)
admin.site.register(DetalleVenta)




