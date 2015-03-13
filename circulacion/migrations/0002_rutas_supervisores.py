# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rutas',
            fields=[
                ('NombreRuta', models.CharField(max_length=35, serialize=False, primary_key=True)),
                ('Colonias', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Rutas',
                'ordering': ['NombreRuta'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='supervisores',
            fields=[
                ('Codigo', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('Nombre', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name_plural': 'Supervisores',
            },
            bases=(models.Model,),
        ),
    ]
