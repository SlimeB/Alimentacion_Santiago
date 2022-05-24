from django.shortcuts import render

# Create your views here.
def home(request):
    n = range(6)
    return render(request, 'home.html', {"n": n})