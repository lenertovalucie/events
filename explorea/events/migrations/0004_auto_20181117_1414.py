# Generated by Django 2.1.3 on 2018-11-17 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventrun',
            name='happens',
        ),
        migrations.AddField(
            model_name='eventrun',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 6, 17, 18, 30)),
        ),
        migrations.AddField(
            model_name='eventrun',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 6, 17, 18, 30)),
        ),
    ]