# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='planes',
            fields=[
                ('CodigoPlan', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Planes',
                'ordering': ['CodigoPlan'],
            },
            bases=(models.Model,),
        ),
    ]
