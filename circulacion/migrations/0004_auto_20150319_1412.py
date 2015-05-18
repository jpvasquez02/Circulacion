# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0003_asesores'),
    ]

    operations = [
        migrations.CreateModel(
            name='ciudades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Municipio', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
                'ordering': ['Departamentos'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Departamentos', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='repartidores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('NombreRepartidor', models.CharField(max_length=140)),
                ('Telefono', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Repartidores',
                'ordering': ['NombreRepartidor'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ciudades',
            name='Departamentos',
            field=models.ForeignKey(to='circulacion.Departamentos'),
            preserve_default=True,
        ),
    ]
