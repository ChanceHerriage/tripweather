# Generated by Django 2.0.7 on 2018-07-21 17:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_auto_20180721_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 21, 17, 51, 35, 949801, tzinfo=utc)),
        ),
    ]
