from django.db import models

# Create your models here.

# crear una clase para cada tabla 

class CLIENTES(models.Model):

    nombre= models.CharField(max_length=30,verbose_name="Nombre Cliente")
    direccion=models.CharField(max_length=50,verbose_name="Direccion Cliente")
    email=models.EmailField(blank=True,null=True,verbose_name="Correo Cliente")
    telefono=models.CharField(max_length=15,verbose_name="Telefono Cliente")

   # def __str__(self):
     #   return self.nombre

class ARTICULOS(models.Model):

    nombrearticulo= models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precioarticulo=models.IntegerField()

    #def __str__(self):
       # return self.nombrearticulo,self.seccion,self.precioarticulo

    # funcion __str__ 
     

        
    #    return'El nombre es %s la Seccion es %s y el Precio es %s' %(self.nombrearticulo,self.seccion,self.precioarticulo)



class PEDIDOS(models.Model):

    numerodepedido=models.IntegerField()
    fechadepedido=models.DateField()
    entrgapedido=models.BooleanField()
