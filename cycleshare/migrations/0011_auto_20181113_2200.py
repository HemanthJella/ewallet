# Generated by Django 2.1.2 on 2018-11-13 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycleshare', '0010_auto_20181107_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cycle',
            old_name='week',
            new_name='hour',
        ),
        migrations.RenameField(
            model_name='cycle',
            old_name='week_sub',
            new_name='hour_sub',
        ),
    ]
