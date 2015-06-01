# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0028_auto_20150530_1003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cierre',
            options={'verbose_name_plural': 'Cierre'},
        ),
        migrations.RemoveField(
            model_name='guia',
            name='Dia',
        ),
        migrations.RemoveField(
            model_name='planes',
            name='Precio',
        ),
    ]
