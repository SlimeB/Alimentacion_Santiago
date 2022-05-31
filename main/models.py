from django.db import models

# Create your models here.

class restaurante(models.Model):
    id_producto = models.IntegerField(null=False, primary_key=True, unique=True),
    nombre_restaurante = models.CharField(max_length=50, blank=False)

class producto(models.Model):
    nombre_producto = models.CharField(max_length=100, blank=False),
    descripcion_producto = models.CharField(max_length=500, blank=False)
    restaurante_producto = models.ForeignKey(to=restaurante, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=False)