from django.shortcuts import render

# Create your views here.
def home(request):
    n = range(6)
    return render(request, 'home.html', {"n": n})

def carrito(request):
    n = [
        {"titulo": "patata", "ingre": "papas, aceite y sal", "rest": "el emporio de las papas"},
        {"titulo": "cebolla caramelizada", "ingre": "cebolla, aceite y azucar", "rest": "mc cebolla"},
    ]

    return render(request, "carrito.html", {"n": n})

def pedido(request):
    return render(request, "pedido.html")