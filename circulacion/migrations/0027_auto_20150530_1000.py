# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0026_auto_20150529_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='guia',
            name='Dia',
            field=models.CharField(default='', choices=[('L', 'Lunes'), ('M', 'Martes'), ('K', 'Miercoles'), ('J', 'Jueves'), ('V', 'Viernes'), ('S', 'Sabado'), ('D', 'Domingo')], max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planes',
            name='Precio',
            field=models.DecimalField(default='', max_digits=7, decimal_places=2),
            preserve_default=False,
        ),
    ]
