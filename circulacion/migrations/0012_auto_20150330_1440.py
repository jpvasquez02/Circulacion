# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0011_auto_20150323_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudades',
            options={'verbose_name_plural': 'Ciudades', 'ordering': ['Departamentos']},
        ),
        migrations.AddField(
            model_name='clientes',
            name='latitud',
            field=models.CharField(max_length=50, default=2015),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientes',
            name='longitud',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
    ]
