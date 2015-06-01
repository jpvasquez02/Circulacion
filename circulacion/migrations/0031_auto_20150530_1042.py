# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0030_auto_20150530_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guia',
            name='Cliente',
        ),
        migrations.RemoveField(
            model_name='guia',
            name='Ruta',
        ),
        migrations.RemoveField(
            model_name='guia',
            name='Supervisor',
        ),
        migrations.DeleteModel(
            name='guia',
        ),
    ]
