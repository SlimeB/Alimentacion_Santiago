from django.shortcuts import render
from .models import producto, restaurante
from .forms import *

# Create your views here.
carritoPedido = list()

def home(request): #listo
    p = producto.objects.all()
    
    if request.method == "POST":
        pr = producto.objects.filter(nombre_producto = request.POST["boton"]).values()[0]
        carritoPedido.append(pr)
    return render(request, 'home.html', {"p": p})

def carrito(request): #listo
    
    n = carritoPedido

    if request.method == "POST":
        for i in carritoPedido:
            if i["id"] == int(request.POST["borrar"]):
                carritoPedido.remove(i)
                break
    return render(request, "carrito.html", {"n": n})

def usuario(request): #listo
    return render(request, "usuario.html")

def pedido(request):
    return render(request, "pedido.html")

def registro_restaurante(request):
    r = registroRestaurante()
    re = restaurante.objects.all()
    return render(request, "registro_restaurante.html", {"r": r, "re": re})

def registro_receta(request):
    r = registroReceta
    p = producto.objects.all()
    return render(request, "registro_receta.html", {"r": r, "p": p})