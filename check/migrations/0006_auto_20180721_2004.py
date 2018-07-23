# Generated by Django 2.0.7 on 2018-07-21 20:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0005_auto_20180721_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 21, 20, 4, 46, 697244, tzinfo=utc)),
        ),
    ]
