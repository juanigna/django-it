# Generated by Django 5.0.1 on 2024-03-04 23:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre del animal')),
                ('raza', models.CharField(choices=[('GD', 'Golden'), ('LD', 'Labrador'), ('RD', 'Ragdoll'), ('SD', 'Saint Bernard'), ('TD', 'Tibetan'), ('WD', 'Wild'), ('OT', 'Otro')], default='OT', max_length=2, verbose_name='Raza del animal')),
                ('categoria', models.CharField(choices=[('CN', 'Canino'), ('FO', 'Felino'), ('OT', 'Otro')], default='OT', max_length=2, verbose_name='Categoria del animal')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre de la enfermedad')),
                ('grado', models.CharField(choices=[('L', 'Leve'), ('M', 'Moderada'), ('H', 'Grave')], max_length=2, verbose_name='Grado de la enfermedad')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre del instructor')),
                ('email', models.EmailField(max_length=60, verbose_name='Email del instructor')),
                ('cursos_asignados', models.IntegerField(verbose_name='Cursos asignados')),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre de la localidad')),
                ('cp', models.CharField(max_length=10, verbose_name='Codigo postal')),
                ('provincia', models.CharField(max_length=60, verbose_name='Provincia')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultaVeterinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de la consulta')),
                ('costo', models.PositiveIntegerField(verbose_name='Costo de la consulta')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='entidad.animal')),
                ('enfermedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidad.enfermedad')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre cliente')),
                ('apellido', models.CharField(max_length=60, verbose_name='Apellido del cliente')),
                ('edad', models.IntegerField(blank=True, null=True, verbose_name='Edad')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_nac', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('tipo_iva', models.CharField(choices=[('CF', 'Consumidor Final'), ('EX', 'Exento'), ('RI', 'Responsable Inscripto'), ('MT', 'Monotributo'), ('OT', 'Otro')], default='CF', max_length=2, verbose_name='Tipo de IVA')),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='entidad.localidad')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='dueno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='entidad.persona'),
        ),
    ]
