"""AlimentacionSantiago URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('car/', views.carrito, name="carrito"),
    path('pedido/', views.pedido, name="pedido"),
    path('registro_restaurante/', views.registro_restaurante, name="registro_restaurante"),
    path('registro_receta/', views.registro_receta, name="registro_receta"),
    path('usuario/', views.usuario, name="usuario"),
    path('nosotros/', views.usuario, name="nosotros"),
]
