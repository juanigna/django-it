import sqlite3
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from .forms import NuevoCliente, NuevoAnimal
from .models import Localidad, Persona, Animal

# Create your views here.
def index(request, template_name="entidad/index.html"):
    return render(request, template_name)


def animales(request, template_name="entidad/animales.html"):
    animales = Animal.objects.all()
    context = {"animales": animales}
    return render(request, template_name, context)

def animalesById(request,id ,template_name="entidad/animal.html"):
    # conn = sqlite3.connect("veterinaria.sqlite3")
    # cliente = conn.cursor()
    # cliente.execute("SELECT nombre, categoria, raza FROM animal WHERE id=?",[id])
    # single_animal = cliente.fetchone()
    # if single_animal is None:
    #     raise Http404
    # conn.close()
    # context = {"animal": single_animal}
    animalById = Animal.objects.get(id=id)
    if animalById is None:
        raise Http404
        
    context = {"animal": animalById}
    return render(request, template_name, context)

def clientes(request, template_name="entidad/clientes.html"):
    personas = Persona.objects.all()
    context = {"clientes": personas}
    return render(request, template_name, context)

def clienteById(request, id ,template_name="entidad/cliente.html"):
    personaById = Persona.objects.get(id=id)
    if personaById is None:
        raise Http404
    context = {"cliente": personaById}
    return render(request, template_name, context)

def nuevoCliente(request, template_name="entidad/nuevo-cliente.html"):
    if request.method == "POST":
        form = NuevoCliente(request.POST)
        if form.is_valid():
            # conn = sqlite3.connect("veterinaria.sqlite3")
            # cliente = conn.cursor()
            # cliente.execute("INSERT INTO cliente VALUES (?, ?, ?, ?)", (form.cleaned_data["num_dni"], form.cleaned_data["nombre"], form.cleaned_data["apellido"], form.cleaned_data["direccion"]))
            # conn.commit()
            # conn.close()
            form.save()
            return redirect("clientes")
    else:
        form = NuevoCliente()
        
    context = {"form": form}
    
    return render(request, template_name, context)

def nuevoAnimal(request, template_name="entidad/nuevo-animal.html"):
    if request.method == "POST":
        form = NuevoAnimal(request.POST)
        if form.is_valid():
            conn = sqlite3.connect("veterinaria.sqlite3")
            cliente = conn.cursor()
            cliente.execute("INSERT INTO animal VALUES (?, ?, ?, ?, ?)", 
                                                    (   
                                                        form.cleaned_data["id"],
                                                        form.cleaned_data["nombre"],
                                                        form.cleaned_data["raza"],
                                                        form.cleaned_data["categoria"],
                                                        form.cleaned_data["dueno"]
                                                    )
            )
            conn.commit()
            conn.close()
            return redirect("animales")
    else:
        form = NuevoAnimal()
    
    context = {"form": form}
    return render(request, template_name, context)

def localidades(request, template_name="entidad/localidades.html"):
    localidades_list = Localidad.objects.all()
    context = {"localidades": localidades_list}
    
    return render(request, template_name, context)