# Generated by Django 2.1.2 on 2018-11-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ID', models.CharField(max_length=100)),
                ('book_ID', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
