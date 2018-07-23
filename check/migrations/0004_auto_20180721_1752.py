# Generated by Django 2.0.7 on 2018-07-21 17:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0003_auto_20180721_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='unique_id',
        ),
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 21, 17, 52, 37, 199301, tzinfo=utc)),
        ),
    ]
