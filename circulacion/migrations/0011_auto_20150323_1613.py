# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0010_auto_20150323_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='ciudades',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Municipio', models.CharField(max_length=140)),
            ],
            options={
                'ordering': ['Departamentos'],
                'verbose_name_plural': 'Departamentos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('Codigo', models.IntegerField(serialize=False, primary_key=True, max_length=10)),
                ('TipoCliente', models.CharField(choices=[('Empresarial', 'Empresarial'), ('Residencial', 'Residencial')], max_length=50)),
                ('Nombre', models.CharField(max_length=140)),
                ('Identificacion', models.CharField(max_length=15)),
                ('FechaNacimiento', models.DateField()),
                ('Genero', models.CharField(max_length=15, null=True, blank=True, choices=[('F', 'Femenino'), ('M', 'Masculino')])),
                ('Telefono', models.IntegerField(max_length=15)),
                ('Celular', models.IntegerField(blank=True, null=True, max_length=15)),
                ('Colonia', models.CharField(max_length=60)),
                ('Calle', models.CharField(max_length=30)),
                ('Avenida', models.CharField(max_length=30)),
                ('Referencia', models.CharField(max_length=140)),
                ('Correo', models.EmailField(max_length=75)),
                ('Ciudad', models.ForeignKey(to='circulacion.ciudades')),
            ],
            options={
                'ordering': ['Nombre'],
                'verbose_name_plural': 'Clientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='departamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Departamentos', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='clientes',
            name='Departamentos',
            field=models.ForeignKey(to='circulacion.departamentos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ciudades',
            name='Departamentos',
            field=models.ForeignKey(to='circulacion.departamentos'),
            preserve_default=True,
        ),
    ]
