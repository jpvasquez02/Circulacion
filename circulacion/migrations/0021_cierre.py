# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0020_tiraje_ruta'),
    ]

    operations = [
        migrations.CreateModel(
            name='cierre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cantidad', models.IntegerField(max_length=5)),
                ('Direccion', models.CharField(max_length=140)),
                ('Valor', models.DecimalField(max_digits=4, decimal_places=2)),
                ('Recibo', models.CharField(max_length=10)),
                ('ValorRecibo', models.DecimalField(max_digits=4, decimal_places=2)),
                ('Comision', models.DecimalField(max_digits=4, decimal_places=2)),
                ('FechaPago', models.DateField()),
                ('Inicio', models.DateField()),
                ('Fin', models.DateField()),
                ('Nombre', models.ForeignKey(to='circulacion.suscripcion')),
                ('Tipo', models.ForeignKey(to='circulacion.planes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
