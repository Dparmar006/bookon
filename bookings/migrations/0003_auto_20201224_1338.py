# Generated by Django 3.1.4 on 2020-12-24 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201209_1247'),
        ('bookings', '0002_auto_20201224_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer'),
        ),
    ]
