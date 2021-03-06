# Generated by Django 3.1.4 on 2021-05-03 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20210310_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='end_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='start_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='average_service_time',
            field=models.DurationField(default=datetime.timedelta(seconds=1500)),
        ),
    ]
