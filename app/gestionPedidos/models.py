from django.db import models


# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion=models.CharField(max_length=50,verbose_name="La Direccion")
    email=models.EmailField(blank=True,null=True)
    fono=models.CharField(max_length=7)

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion= models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return ' El nombre es {0} , la seccion es {1} , el precio es {2} '.format(self.nombre,self.seccion, self.precio)


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha= models.DateField()
    entregado = models.BooleanField( )
