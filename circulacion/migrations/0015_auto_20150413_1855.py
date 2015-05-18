# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0014_suscripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscripcion',
            name='Repartidor',
            field=models.ForeignKey(to='circulacion.repartidores'),
            preserve_default=True,
        ),
    ]
