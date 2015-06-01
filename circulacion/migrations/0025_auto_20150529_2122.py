# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0024_auto_20150529_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guia',
            name='Fecha',
            field=models.DateField(auto_now_add=True, auto_now=True),
            preserve_default=True,
        ),
    ]
