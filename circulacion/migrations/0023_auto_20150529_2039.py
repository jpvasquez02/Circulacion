# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0022_recibo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guia',
            name='Supervisor',
            field=models.ForeignKey(to='circulacion.supervisores', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='suscripcion',
            name='Valor',
            field=models.DecimalField(max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
    ]
