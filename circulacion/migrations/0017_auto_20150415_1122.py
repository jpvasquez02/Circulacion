# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0016_remove_suscripcion_vencimiento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suscripcion',
            options={'verbose_name_plural': 'Suscripciones', 'ordering': ['Codigo', 'Suscriptor']},
        ),
    ]
