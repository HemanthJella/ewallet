# Generated by Django 2.0.9 on 2018-12-10 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_profile_student_id'),
        ('student', '0002_auto_20181113_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='toprofile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='dashboard.Profile'),
        ),
    ]
