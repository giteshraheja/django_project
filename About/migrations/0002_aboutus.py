# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-14 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
