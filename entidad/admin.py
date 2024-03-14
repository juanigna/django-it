from django.contrib import admin
from .models import Animal, Persona, Localidad, Enfermedad, Consulta    

# Register your models here.
admin.site.register(Animal)
admin.site.register(Persona)
admin.site.register(Localidad)
admin.site.register(Enfermedad)
admin.site.register(Consulta)   
