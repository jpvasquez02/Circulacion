# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0025_auto_20150529_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guia',
            name='Cortesias',
            field=models.IntegerField(blank=True, max_length=5, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guia',
            name='Destino',
            field=models.CharField(blank=True, max_length=140, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guia',
            name='Envios',
            field=models.IntegerField(blank=True, max_length=5, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guia',
            name='Suscripciones',
            field=models.IntegerField(blank=True, max_length=5, null=True),
            preserve_default=True,
        ),
    ]
