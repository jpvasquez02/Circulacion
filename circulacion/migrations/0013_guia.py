# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0012_auto_20150330_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='guia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Fecha', models.DateField()),
                ('Destino', models.CharField(max_length=140)),
                ('Envios', models.IntegerField(max_length=5)),
                ('Cortesias', models.IntegerField(max_length=5)),
                ('Suscripciones', models.IntegerField(max_length=5)),
                ('Cliente', models.ForeignKey(to='circulacion.clientes')),
                ('Ruta', models.ForeignKey(to='circulacion.rutas')),
                ('Supervisor', models.ForeignKey(to='circulacion.supervisores')),
            ],
            options={
                'ordering': ['Ruta'],
                'verbose_name_plural': 'Guía Producción',
            },
            bases=(models.Model,),
        ),
    ]
