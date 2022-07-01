from pyexpat import model
from statistics import mode
from venv import create
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField







# Create your models here.


def cargarFotoProducto(instance, filename):
    return "fotosProductos/foto_{0}_{1}".format(instance.idProducto,filename)


class Producto(models.Model):
    idProducto = models.CharField(max_length=5, primary_key=True)
    marcaProducto = models.CharField(max_length=30, blank=True, null=True)
    nombreProducto = models.CharField(max_length=30, blank=True, null=True)
    stock   = models.IntegerField(blank=True, null=True)
    precio   = models.IntegerField(blank=True, null=True)
    foto = models.ImageField(upload_to=cargarFotoProducto, null=True)
    activo = models.IntegerField(blank=True, null=True)  

    def __str__(self):
        return self.idProducto+", "+self.marcaProducto+", "+self.nombreProducto+", "+str(self.stock)\
               +", "+str(self.precio)+", "+self.foto.__str__()



def cargarFotoPersona(instance, filename):
    return "fotosPersonas/foto_{0}_{1}".format(instance.idPersona,filename)


class Personas(models.Model):

    tiposUsuario = models.TextChoices('Adminstrador', 'Usuario')

    idPersona = models.CharField(max_length=5, primary_key=True)
    nombrePersona = models.CharField(max_length=30, blank=True, null=True)
    usuario = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    contrasena = models.CharField(max_length=30, blank=True, null=True)
    tipoUsuario = models.CharField(blank=True,choices=tiposUsuario.choices, max_length=30)
    foto = models.ImageField(upload_to=cargarFotoProducto, null=True)
    activo = models.IntegerField(blank=True, null=True) 
    

    def __str__(self):
        return self.idPersona+", "+self.nombrePersona+", "+self.usuario+", "+self.email+", "+self.contrasena+", "+self.tipoUsuario\
               +", "+self.foto.__str__()


def cargarFotoProducto(instance, filename):
    return "fotosProductos/foto_{0}_{1}".format(instance.idProducto,filename)


############# VENTAS Y DETALE_VENTA ############################

User = get_user_model()


class Venta(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return str(self.id)
    
    @property
    def total(self):
        return self.detalleventa_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table='Ventas'
        verbose_name ='Ventas'
        verbose_name_plural='Ventas'
        ordering=['id']

class DetalleVenta(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto  = models.ForeignKey(Producto, on_delete=models.CASCADE,blank=True, null=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombreProducto}'


    class Meta:
        db_table='DetalleVenta'
        verbose_name ='DetalleVenta'
        verbose_name_plural='DetalleVenta'
        ordering=['id']
    





