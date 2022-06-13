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
    re = restaurante.objects.all()

    if request.method == "POST":
        print(request.POST.get)
        r = registroRestaurante(request.POST)
        if r.is_valid():
            n = r.cleaned_data["nombre_restaurante"]
            res = restaurante(nombre_restaurante = n)
            res.save()
    else:
        r = registroRestaurante()
    return render(request, "registro_restaurante.html", {"r": r, "re": re})

def registro_receta(request):
    p = producto.objects.all()

    if request.method == "POST":
        r = registroReceta(request.POST)
        if r.is_valid():
            n = r.cleaned_data["nombre_receta"]
            de = r.cleaned_data["descripcion_producto"]
            di = r.cleaned_data["disponible"]
            pr = producto(nombre_producto= n, descripcion_producto= de, restaurante_producto= restaurante.objects.filter(nombre_restaurante = "papamania")[0], disponible= di)
            pr.save()
    else:
        r = registroReceta()
    return render(request, "registro_receta.html", {"r": r, "p": p})

def nosotros(request):
    return render(request, "nosotros.html", {})