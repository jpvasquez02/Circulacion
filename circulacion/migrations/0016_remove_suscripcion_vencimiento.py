# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0015_auto_20150413_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suscripcion',
            name='Vencimiento',
        ),
    ]
