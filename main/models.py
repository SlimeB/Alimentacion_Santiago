from django.db import models

# Create your models here.

class restaurante(models.Model):
    nombre_restaurante = models.CharField(max_length=50, blank=False)
    
    def __str__(self) -> str:
        return self.nombre_restaurante

class producto(models.Model):
    nombre_producto = models.CharField(max_length=100, blank=False, default="a")
    descripcion_producto = models.CharField(max_length=500, blank=False)
    restaurante_producto = models.ForeignKey(to=restaurante,blank=False, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre_producto

class categoria_usuario(models.Model):
    id_categoria = models.IntegerField(primary_key=True, blank= False, unique= True)
    nombre_categoria = models.CharField(max_length= 80, blank=False, unique=True)
    
    def __str__(self):
        return self.nombre_categoria

class usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100, blank=False)
    contraseña_usuario = models.CharField(max_length=20, blank=False)
    categoria_usuario = models.ForeignKey(to=categoria_usuario, blank= False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_usuario