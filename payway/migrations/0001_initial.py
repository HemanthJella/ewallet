# Generated by Django 2.0.9 on 2018-12-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paywaylog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('flag', models.IntegerField()),
                ('cardid', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
            ],
        ),
    ]
