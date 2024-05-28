# Generated by Django 5.0 on 2024-05-01 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymManagement', '0005_plan_period_alter_attendance_workouttime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='name',
            field=models.CharField(default='normal', max_length=50),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='workoutTime',
            field=models.TimeField(default=datetime.datetime(2024, 5, 1, 13, 14, 4, 774195)),
        ),
        migrations.AlterField(
            model_name='gymmember',
            name='paidAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 1, 13, 14, 4, 774195)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 1, 13, 14, 4, 774195)),
        ),
    ]
