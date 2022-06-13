from django import forms
from .models import restaurante

class registroRestaurante(forms.Form):
    nombre_restaurante = forms.CharField(max_length=50, required=True)

class registroReceta(forms.Form):
    nombre_receta = forms.CharField(max_length=100, required=True)
    descripcion_producto = forms.CharField(max_length=500, required=True, widget=forms.Textarea)
    disponible = forms.BooleanField(required=True)