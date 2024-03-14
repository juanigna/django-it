
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),

    #Login y register
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    
    #Animales
    path("animales/", views.animales, name="animales"),
    path("animales/<int:id>", views.animalesById, name="animal"),
    path("animales/nuevo", views.nuevoAnimal, name="nuevo-animal"),
    path("animales/modificar/<int:id>", views.modificarAnimal, name="modificar-animal"),
    path('animales/eliminar/<int:id>', views.elimiarAnimal, name="eliminar-animal"),

    
    #Clientes
    path("clientes/", views.clientes, name="clientes"),
    path('clientes/<int:id>', views.clienteById, name="cliente"),
    path('clientes/nuevo', views.nuevoCliente, name="nuevo-cliente"),
    path('clientes/modificar/<int:id>', views.modificarCliente, name="modificar-cliente"),
    path('clientes/eliminar/<int:id>', views.elimiarCliente, name="eliminar-cliente"),
    
    #Localidades
    path('localidades/nuevo', views.nuevaLocalidad, name="nueva-localidad"),
    path('localidades/', views.localidades, name="localidades"),
    path('localidades/<int:id>', views.localidad, name="localidad"),

    #Enfermedades
    path('enfermedades/nuevo', views.nuevaEnfermedad, name="nueva-enfermedad"),
    path('enfermedades/', views.enfermedades, name="enfermedades"),

    #Consultas
    path('consultas/nuevo', views.nuevaConsulta, name="nueva-consulta"),
    path('consultas/', views.consultas, name="consultas"),
]