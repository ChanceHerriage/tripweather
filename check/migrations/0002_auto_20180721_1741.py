# Generated by Django 2.0.7 on 2018-07-21 17:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='name',
            field=models.CharField(default='default_name', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 21, 17, 41, 18, 294349, tzinfo=utc)),
        ),
    ]
