# Generated by Django 3.1.4 on 2020-12-08 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201208_1859'),
        ('services', '0002_service_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='averageServiceTime',
            new_name='average_service_time',
        ),
        migrations.AlterField(
            model_name='service',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.owner'),
        ),
    ]
