# Generated by Django 2.1.2 on 2018-11-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0002_librarian_due'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='librarian',
            name='id',
        ),
        migrations.AlterField(
            model_name='librarian',
            name='book_ID',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
