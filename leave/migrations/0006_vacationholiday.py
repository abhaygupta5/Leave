# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-09 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0005_closedholiday_restrictedholiday'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacationHoliday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
    ]
