from django import forms
from django.forms import ModelForm
from entidad.models import Localidad, Persona

class NuevoCliente(ModelForm):
    class Meta:
        model = Persona
        fields = ["nombre","apellido","edad","localidad","email","activo","fecha_nac","tipo_iva"]
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "edad": forms.NumberInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "activo": forms.CheckboxInput(attrs={'class': 'form-control'}),
            "fecha_nac": forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            "tipo_iva": forms.Select(attrs={'class': 'form-control'}),
        }

class NuevoAnimal(forms.Form):
    id = forms.IntegerField(label="Id del animal", max_value=99999999)
    nombre = forms.CharField(label="Nombre del animal", max_length=100)
    RAZA = (
        (1, 'Perro'),
        (2, 'Gato'),
        (3, 'Conejo'),
        (4, 'Caballo'),
        (5, 'Otro')
    )
    raza = forms.ChoiceField(label="Raza", choices=RAZA)
    CATEGORIA = (
        (1, 'Canino'),
        (2, 'Felino'),
        (4, 'Otro')
    )
    categoria = forms.ChoiceField(label="Categoria", choices=CATEGORIA)
    dueno = forms.IntegerField(label="Dni del dueño", max_value=99999999)