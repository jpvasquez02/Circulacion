# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0027_auto_20150530_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guia',
            name='Dia',
            field=models.CharField(blank=True, choices=[('L', 'Lunes'), ('M', 'Martes'), ('K', 'Miercoles'), ('J', 'Jueves'), ('V', 'Viernes'), ('S', 'Sabado'), ('D', 'Domingo')], null=True, max_length=10),
            preserve_default=True,
        ),
    ]
