# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-30 20:08
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dummy_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummyimage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='static/images'),
        ),
    ]
