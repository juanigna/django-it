from django import forms
from django.forms import ModelForm
from entidad.models import Animal, Consulta, Enfermedad, Localidad, Persona
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
    

class DateInput(forms.DateInput):
    input_type = 'date'

class NuevoCliente(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        exclude = ["activo"]
        widgets = {
            "fecha_nac": DateInput(
                attrs={'type': 'date', 'class': 'form-control input'}
            ),
            "nombre": forms.TextInput(
                attrs= {'class': 'form-control input'}
            ),
            "apellido": forms.TextInput(
                attrs= {'class': 'form-control input'}
            ),
            "edad": forms.NumberInput(
                attrs= {'class': 'form-control input'}
            ),
            "localidad": forms.Select(
                attrs= {'class': 'form-control input'}
            ),
            "email": forms.EmailInput(
                attrs= {'class': 'form-control input'}
            ),
            "tipo_iva": forms.Select(
                attrs= {'class': 'form-control input'}
            ),
            
        }

class NuevoAnimal(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        exclude = ["activo"]
        widgets = {
            "nombre": forms.TextInput(
                attrs= {'class': 'form-control input'}
            ),
            "raza": forms.Select(
                attrs= {'class': 'form-control input'}
            ),
            "categoria": forms.Select(
                attrs= {'class': 'form-control input'}
            ),
            "dueno": forms.Select(
                attrs= {'class': 'form-control input'}
            ),
        }


class NuevaLocalidad(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

class NuevaEnfermedad(ModelForm):
    class Meta:
        model = Enfermedad
        fields = '__all__'
        

class NuevaConsulta(ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {
            "fecha": DateInput(
                attrs={'type': 'date'}
            ),
        }