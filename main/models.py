from django.db import models

# Create your models here.

class restaurante(models.Model):
    id_producto = models.IntegerField(null=False, primary_key=True, unique=True),
    nombre_restaurante = models.CharField(max_length=50, blank=False)

class producto(models.Model):
    nombre_producto = models.CharField(max_length=100, blank=False),
    descripcion_producto = models.CharField(max_length=500, blank=False)
    restaurante_producto = models.ForeignKey(to=restaurante,blank=False, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=False)

class categoria_usuario(models.Model):
    id_categoria = models.IntegerField(primary_key=True, blank= False, unique= True)
    nombre_categoria = models.CharField(max_length= 80, blank=False, unique=True)

class usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100, blank=False)
    contraseña_usuario = models.CharField(max_length=20, blank=False)
    categoria_usuario = models.ForeignKey(to=categoria_usuario, blank= False, on_delete=models.CASCADE)