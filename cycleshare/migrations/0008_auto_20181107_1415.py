# Generated by Django 2.1.2 on 2018-11-07 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycleshare', '0007_avalability'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='avalability',
            new_name='q',
        ),
        migrations.RemoveField(
            model_name='cycle',
            name='month_sub',
        ),
    ]
