# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0029_auto_20150530_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tiraje',
            name='ruta',
        ),
        migrations.DeleteModel(
            name='tiraje',
        ),
    ]
