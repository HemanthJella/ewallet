# Generated by Django 2.1.2 on 2018-11-11 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mess', '0003_auto_20181110_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponsBought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boughtTime', models.DateTimeField()),
                ('couponId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='couponsdold', to='mess.Coupons')),
            ],
        ),
    ]
