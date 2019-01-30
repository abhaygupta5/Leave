# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-01-25 18:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leave', '0006_vacationholiday'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveOffline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(blank=True, default='', max_length=500)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('application_date', models.DateField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_leaves_offline', to=settings.AUTH_USER_MODEL)),
                ('leave_user_select', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveSegmentOffline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(null=True, upload_to='leave/leave_documents/')),
                ('start_date', models.DateField()),
                ('start_half', models.BooleanField(default=False)),
                ('end_date', models.DateField()),
                ('end_half', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='segments_offline', to='leave.LeaveOffline')),
                ('leave_type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leave.LeaveType')),
            ],
        ),
        migrations.CreateModel(
            name='ReplacementSegmentOffline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replacement_type', models.CharField(choices=[('academic', 'Academic Replacement'), ('administrative', 'Administrative Replacement')], default='academic', max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replace_segments_offline', to='leave.LeaveOffline')),
                ('replacer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rep_requests_offline', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='leavescount',
            name='year',
            field=models.IntegerField(default=2019),
        ),
    ]
