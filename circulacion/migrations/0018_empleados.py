# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0017_auto_20150415_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=140)),
                ('Puesto', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name_plural': 'Empleados',
            },
            bases=(models.Model,),
        ),
    ]
