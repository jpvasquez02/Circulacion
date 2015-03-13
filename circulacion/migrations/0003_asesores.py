# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0002_rutas_supervisores'),
    ]

    operations = [
        migrations.CreateModel(
            name='asesores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('NombreAsesor', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Asesores',
                'ordering': ['NombreAsesor'],
            },
            bases=(models.Model,),
        ),
    ]
