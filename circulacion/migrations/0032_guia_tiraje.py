# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0031_auto_20150530_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='guia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('Fecha', models.DateField(auto_now=True, auto_now_add=True)),
                ('Destino', models.CharField(blank=True, null=True, max_length=140)),
                ('Envios', models.IntegerField(blank=True, null=True, max_length=5)),
                ('Cortesias', models.IntegerField(blank=True, null=True, max_length=5)),
                ('Suscripciones', models.IntegerField(blank=True, null=True, max_length=5)),
                ('Cliente', models.ForeignKey(to='circulacion.clientes')),
                ('Ruta', models.ForeignKey(to='circulacion.rutas')),
                ('Supervisor', models.ForeignKey(blank=True, to='circulacion.supervisores', null=True)),
            ],
            options={
                'verbose_name_plural': 'Guía Producción',
                'ordering': ['Ruta'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tiraje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('lunes', models.IntegerField(max_length=5)),
                ('martes', models.IntegerField(max_length=5)),
                ('miercoles', models.IntegerField(max_length=5)),
                ('jueves', models.IntegerField(max_length=5)),
                ('viernes', models.IntegerField(max_length=5)),
                ('sabado', models.IntegerField(max_length=5)),
                ('domingo', models.IntegerField(max_length=5)),
                ('ruta', models.ForeignKey(to='circulacion.rutas')),
            ],
            options={
                'verbose_name_plural': 'Tiraje',
            },
            bases=(models.Model,),
        ),
    ]
