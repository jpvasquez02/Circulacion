# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0018_empleados'),
    ]

    operations = [
        migrations.CreateModel(
            name='tiraje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('lunes', models.IntegerField(max_length=5)),
                ('martes', models.IntegerField(max_length=5)),
                ('miercoles', models.IntegerField(max_length=5)),
                ('jueves', models.IntegerField(max_length=5)),
                ('viernes', models.IntegerField(max_length=5)),
                ('sabado', models.IntegerField(max_length=5)),
                ('domingo', models.IntegerField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Tiraje',
            },
            bases=(models.Model,),
        ),
    ]
