# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0007_auto_20150319_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudades',
            name='Departamentos',
            field=models.ForeignKey(to='circulacion.departamentos'),
            preserve_default=True,
        ),
    ]
