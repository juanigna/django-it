from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm, NuevaConsulta, NuevaEnfermedad, NuevaLocalidad, NuevoCliente, NuevoAnimal
from .models import Consulta, Enfermedad, Localidad, Persona, Animal
from .forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request, template_name="entidad/register.html"):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form.save()
        return redirect('index')
    context = {"form": form}
    return render(request, template_name, context)

def login(request, template_name="entidad/login.html"):
    form = LoginForm()
    if(request.method == "POST"):
        form = LoginForm(request, data=request.POST)

        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:

                auth.login(request, user)

                return redirect("index")
        
        print(username)
    
    context = {"form": form}
    
    return render(request, template_name, context)


def logout(request):
    
    auth.logout(request)
    
    return redirect("login")


@login_required
def index(request, template_name="entidad/index.html"):
    return render(request, template_name)


def animales(request, template_name="entidad/animales.html"):
    animales = Animal.objects.filter(activo=True)
    context = {"animales": animales}
    return render(request, template_name, context)

def animalesById(request,id ,template_name="entidad/animal.html"):
    animalById = Animal.objects.get(id=id)
    if animalById is None:
        raise Http404
        
    context = {"animal": animalById}
    return render(request, template_name, context)

@login_required
def modificarAnimal(request, id, template_name="entidad/modificar-animal.html"):
    animal = Animal.objects.get(id=id)
    
    if request.method == "POST":
        form = NuevoAnimal(request.POST or None, instance=animal)
        if form.is_valid():
            form.save()
            return redirect("animales")
    else:
        form = NuevoAnimal(instance=animal)
    
    context = {"form": form}
    return render(request, template_name, context)

@login_required
def elimiarAnimal(request, id, template_name="entidad/confirmar-eliminacion.html"):
    animal = Animal.objects.get(id=id)
    if request.method == "POST":
        animal.activo = False
        animal.save()
        return redirect("animales")
    context = {"dato": animal.nombre, "cancel_url": "animales"}
    return render(request, template_name, context)

def clientes(request, template_name="entidad/clientes.html"):
    personas = Persona.objects.filter(activo=True)
    context = {"clientes": personas}
    return render(request, template_name, context)

def clienteById(request, id ,template_name="entidad/cliente.html"):
    personaById = Persona.objects.get(id=id)
    if personaById is None:
        raise Http404
    context = {"cliente": personaById}
    return render(request, template_name, context)

@login_required
def modificarCliente(request, id, template_name="entidad/modificar-cliente.html"):
    cliente = Persona.objects.get(id=id)
    
    if request.method == "POST":
        form = NuevoCliente(request.POST or None, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("clientes")
    else:
        form = NuevoCliente(instance=cliente)
    
    context = {"form": form}
    return render(request, template_name, context)

@login_required
def elimiarCliente(request, id, template_name="entidad/eliminar-cliente.html"):
    cliente = Persona.objects.get(id=id)
    if request.method == "POST":
        cliente.activo = False
        cliente.save()
        return redirect("clientes")
    context = {"form": cliente}
    return render(request, template_name, context)

@login_required
def nuevoCliente(request, template_name="entidad/nuevo-cliente.html"):
    if request.method == "POST":
        form = NuevoCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes")
    else:
        form = NuevoCliente()
        
    context = {"form": form}
    
    return render(request, template_name, context)

@login_required
def nuevoAnimal(request, template_name="entidad/nuevo-animal.html"):
    
    if request.method == "POST":
        form = NuevoAnimal(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('animales')
    else:
        form = NuevoAnimal()

    context = {"form": form}

    return render(request, template_name, context)

@login_required
def nuevaLocalidad(request, template_name="entidad/nueva-localidad.html"):
    if request.method == "POST":
        form = NuevaLocalidad(request.POST)
        if form.is_valid():
            form.save(commit=True)
            redirect('localidades')
    else:
        form = NuevaLocalidad()
        
    context = {"form": form}
    
    return render(request, template_name, context)

def localidades(request, template_name="entidad/localidades.html"):
    localidades_list = Localidad.objects.all()
    context = {"localidades": localidades_list}
    return render(request, template_name, context)

def localidad(request, id, template_name="entidad/localidad.html"):
    localidadById = Localidad.objects.get(id=id)
    if localidadById is None:
        raise Http404
        
    context = {"localidad": localidadById}
    return render(request, template_name, context)

@login_required
def nuevaEnfermedad(request, template_name="entidad/nueva-enfermedad.html"):
    if request.method == 'POST':
        form = NuevaEnfermedad(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('enfermedades')
    else:
        form = NuevaEnfermedad()
        
    context = {'form': form}
    
    return render(request, template_name, context)

def enfermedades(request, template_name="entidad/enfermedades.html"):
    enfermedades_list = Enfermedad.objects.all()
    context = {"enfermedades": enfermedades_list}
    return render(request, template_name, context)

@login_required
def nuevaConsulta(request, template_name="entidad/nueva-consulta.html"):
    if request.method == "POST":
        form = NuevaConsulta(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('consultas')
    else:
        form = NuevaConsulta()

    context = {"form": form}

    return render(request, template_name, context)

def consultas(request, template_name="entidad/consultas.html"):
    consultas_list = Consulta.objects.all()
    context = {"consultas": consultas_list}
    return render(request, template_name, context)