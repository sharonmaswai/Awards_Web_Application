# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-04 12:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awaards', '0008_auto_20190704_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]