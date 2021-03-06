# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-03 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('awaards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='projects/')),
                ('usability', models.IntegerField(default=0)),
                ('content', models.IntegerField(default=0)),
                ('link', url_or_relative_url_field.fields.URLOrRelativeURLField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
