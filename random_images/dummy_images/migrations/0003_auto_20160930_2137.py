# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-30 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy_images', '0002_auto_20160930_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummyimage',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
