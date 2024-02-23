
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("animales/", views.animales, name="animales"),
    path("animales/<int:id>", views.animalesById, name="animal"),
    path("clientes/", views.clientes, name="clientes"),
    path('clientes/<int:id>', views.clienteById, name="cliente"),
    path('clientes/nuevo', views.nuevoCliente, name="nuevo-cliente"),
    path("animales/nuevo", views.nuevoAnimal, name="nuevo-animal"),
    path('localidades/', views.localidades, name="localidades"),
]