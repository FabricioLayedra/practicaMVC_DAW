# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practica_mvc', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='estado',
            field=models.CharField(choices=[(b'Pagado', b'Pagado'), (b'Pendiente', b'Pendiente'), (b'Acumulado', b'Acumulado')], default=b'acumulado', max_length=25),
        ),
    ]
