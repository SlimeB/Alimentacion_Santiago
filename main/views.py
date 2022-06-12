from django.shortcuts import render
from .models import producto

# Create your views here.
carritoPedido = list()

def home(request):
    p = producto.objects.all()
    
    if request.method == "POST":
        pr = producto.objects.filter(nombre_producto = request.POST["boton"]).values()[0]
        carritoPedido.append(pr)
    return render(request, 'home.html', {"p": p})

def carrito(request):
    n = carritoPedido

    if request.method == "POST":
        for i in carritoPedido:
            if i["id"] == int(request.POST["borrar"]):
                carritoPedido.remove(i)
                break
    return render(request, "carrito.html", {"n": n})

def pedido(request):
    return render(request, "pedido.html")