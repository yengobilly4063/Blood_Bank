# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-01 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood_client',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
