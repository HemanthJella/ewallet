# Generated by Django 2.1.2 on 2018-11-09 07:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons',
            name='addTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 9, 7, 23, 44, 831492, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='coupons',
            name='valid',
            field=models.BooleanField(default=1),
        ),
    ]
