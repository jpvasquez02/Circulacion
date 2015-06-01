# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0021_cierre'),
    ]

    operations = [
        migrations.CreateModel(
            name='recibo',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha', models.DateField()),
                ('Tipo', models.CharField(choices=[('Canje', 'Canje'), ('Certificado', 'Certificado'), ('Cortesia', 'Cortesia'), ('DxP', 'DxP'), ('Pagado', 'Pagado')], max_length=15)),
                ('Descripcion', models.TextField()),
                ('Valor', models.DecimalField(max_digits=5, decimal_places=2)),
                ('Nombre', models.ForeignKey(to='circulacion.clientes')),
                ('Plan', models.ForeignKey(to='circulacion.planes')),
            ],
            options={
                'verbose_name_plural': 'Recibo',
            },
            bases=(models.Model,),
        ),
    ]
