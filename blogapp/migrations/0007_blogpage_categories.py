# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 14:05
from __future__ import unicode_literals

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_blogcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blogapp.BlogCategory'),
        ),
    ]
