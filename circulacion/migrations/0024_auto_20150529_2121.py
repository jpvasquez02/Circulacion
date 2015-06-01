# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0023_auto_20150529_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guia',
            name='Fecha',
            field=models.DateField(auto_now=True),
            preserve_default=True,
        ),
    ]
