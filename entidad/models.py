from django.db import models

TIPO_IVA_CHOICES = (
    ("CF", "Consumidor Final"),
    ("EX", "Exento"),
    ("RI", "Responsable Inscripto"),
    ("MT", "Monotributo"),
    ("OT", "Otro")
)

TIPO_RAZAS_CHOICES = (
    ("GD", "Golden"),
    ("LD", "Labrador"),
    ("RD", "Ragdoll"),
    ("SD", "Saint Bernard"),
    ("TD", "Tibetan"),
    ("WD", "Wild"),
    ("OT", "Otro")
)

TIPO_CATEGORIA_CHOICES = (
        ("CN", 'Canino'),
        ("FO", 'Felino'),
        ("OT", 'Otro')
    )

TIPO_ENFERMEDAD_CHOICES = (
    ("L", "Leve"),
    ("M", "Moderada"),
    ("H", "Grave")
)

class Localidad(models.Model):
    nombre = models.CharField("Nombre de la localidad", max_length=60)
    cp = models.CharField("Codigo postal", max_length=10)
    provincia = models.CharField("Provincia", max_length=60)
    
    def __str__(self):
        return self.nombre + " - " + " " + self.cp + " - " + self.provincia


class Persona(models.Model):
    nombre = models.CharField("Nombre cliente", max_length=60)
    apellido = models.CharField("Apellido del cliente", max_length=60)
    edad = models.IntegerField("Edad", null=True, blank=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_nac = models.DateField("Fecha de nacimiento", null=True, blank=True)
    tipo_iva = models.CharField("Tipo de IVA", max_length=2, choices=TIPO_IVA_CHOICES, default="CF")

    def __str__(self):
        return self.nombre


class Instructor(models.Model):
    nombre = models.CharField("Nombre del instructor", max_length=60)
    email = models.EmailField("Email del instructor", max_length=60)
    cursos_asignados = models.IntegerField("Cursos asignados")


class Animal(models.Model):
    nombre = models.CharField("Nombre del animal", max_length=60)
    raza = models.CharField("Raza del animal", max_length=2, choices=TIPO_RAZAS_CHOICES, default="OT")
    categoria = models.CharField("Categoria del animal", max_length=2, choices=TIPO_CATEGORIA_CHOICES, default="OT")
    dueno = models.ForeignKey(Persona, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    
    def __str__(self):
        return self.nombre + ", " + self.dueno.nombre

class Enfermedad(models.Model):
    nombre = models.CharField("Nombre de la enfermedad", max_length=60)
    grado = models.CharField("Grado de la enfermedad", max_length=2, choices=TIPO_ENFERMEDAD_CHOICES)

    def __str__(self):
        return self.nombre


class Consulta(models.Model):
    fecha = models.DateField("Fecha de la consulta")
    costo = models.PositiveIntegerField("Costo de la consulta")
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Consulta: {self.animal} - {self.animal.dueno.nombre}"