# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-01 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0003_auto_20170702_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approved',
            name='approved',
            field=models.CharField(choices=[('T', 'True'), ('F', 'False')], default='F', max_length=1),
        ),
    ]
