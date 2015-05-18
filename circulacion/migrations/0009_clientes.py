# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0008_auto_20150319_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('Codigo', models.IntegerField(serialize=False, primary_key=True, max_length=10)),
                ('TipoCliente', models.CharField(max_length=50, choices=[('Empresarial', 'Empresarial'), ('Residencial', 'Residencial')])),
                ('Nombre', models.CharField(max_length=140)),
                ('Identificacion', models.CharField(max_length=15)),
                ('FechaNacimiento', models.DateField()),
                ('Genero', models.CharField(blank=True, max_length=15, choices=[('F', 'Femenino'), ('M', 'Masculino')], null=True)),
                ('Telefono', models.IntegerField(max_length=15)),
                ('Celular', models.IntegerField(blank=True, max_length=15, null=True)),
                ('Colonia', models.CharField(max_length=60)),
                ('Calle', models.CharField(max_length=30)),
                ('Avenida', models.CharField(max_length=30)),
                ('Referencia', models.CharField(max_length=140)),
                ('Correo', models.EmailField(max_length=75)),
                ('Ciudad', models.ForeignKey(to='circulacion.ciudades')),
                ('Departamentos', models.ForeignKey(to='circulacion.departamentos')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'ordering': ['Nombre'],
            },
            bases=(models.Model,),
        ),
    ]
