# Generated by Django 3.1.4 on 2020-12-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20201217_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]