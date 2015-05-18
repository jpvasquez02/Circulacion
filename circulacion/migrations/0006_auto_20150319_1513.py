# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0005_auto_20150319_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='control',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, max_length=10, serialize=False)),
                ('fecha', models.DateField()),
                ('opcion', models.CharField(choices=[(1, 'Faltaron X Vendedores'), (2, 'Semaforo en mal Estado'), (3, 'Falta de Energia Electrica'), (4, 'Calle Cerrada'), (5, 'Manifestacion')], max_length=140)),
                ('comentarios', models.TextField()),
                ('supervisor', models.ForeignKey(to='circulacion.supervisores')),
            ],
            options={
                'verbose_name_plural': 'Hoja de Control',
                'ordering': ['fecha'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='ciudades',
            name='Departamentos',
            field=models.ForeignKey(to='circulacion.departamentos'),
            preserve_default=True,
        ),
    ]
