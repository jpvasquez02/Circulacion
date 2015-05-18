# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0013_guia'),
    ]

    operations = [
        migrations.CreateModel(
            name='suscripcion',
            fields=[
                ('Codigo', models.IntegerField(serialize=False, primary_key=True, max_length=10)),
                ('Empresa', models.CharField(max_length=50, choices=[('Empresarial', 'Empresarial'), ('Residencial', 'Residencial')])),
                ('Vencimiento', models.DateField()),
                ('Cantidad', models.IntegerField(max_length=5)),
                ('Valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Contrato', models.IntegerField()),
                ('Recibo', models.IntegerField()),
                ('Entrega', models.CharField(max_length=4, choices=[('L-D', 'L-D'), ('L-S', 'L-S'), ('L-V', 'L-V')])),
                ('Comentarios', models.CharField(max_length=140)),
                ('Tipo', models.CharField(max_length=15, choices=[('Canje', 'Canje'), ('Certificado', 'Certificado'), ('Cortesia', 'Cortesia'), ('DxP', 'DxP'), ('Pagado', 'Pagado')])),
                ('Inicio', models.DateField()),
                ('Fin', models.DateField()),
                ('Repartidor', models.CharField(max_length=50)),
                ('Asesor', models.ForeignKey(to='circulacion.asesores')),
                ('Plan', models.ForeignKey(to='circulacion.planes')),
                ('Ruta', models.ForeignKey(to='circulacion.rutas')),
                ('Suscriptor', models.ForeignKey(to='circulacion.clientes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
