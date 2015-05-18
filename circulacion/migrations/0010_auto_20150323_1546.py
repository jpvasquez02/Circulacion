# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0009_clientes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ciudades',
            name='Departamentos',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='Ciudad',
        ),
        migrations.DeleteModel(
            name='ciudades',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='Departamentos',
        ),
        migrations.DeleteModel(
            name='clientes',
        ),
        migrations.DeleteModel(
            name='Departamentos',
        ),
    ]
