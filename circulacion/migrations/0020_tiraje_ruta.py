# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0019_tiraje'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiraje',
            name='ruta',
            field=models.ForeignKey(default='', to='circulacion.rutas'),
            preserve_default=False,
        ),
    ]
