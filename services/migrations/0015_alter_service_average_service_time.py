# Generated by Django 3.2.1 on 2021-05-17 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_auto_20210504_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='average_service_time',
            field=models.DurationField(blank=True, default=datetime.timedelta(seconds=1500), null=True),
        ),
    ]