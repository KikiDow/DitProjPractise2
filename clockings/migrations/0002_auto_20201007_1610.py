# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-10-07 16:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clockings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='officer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='officer', to=settings.AUTH_USER_MODEL),
        ),
    ]
