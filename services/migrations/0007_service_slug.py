# Generated by Django 3.1.4 on 2020-12-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20201214_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default='default-slug', verbose_name='Slug'),
        ),
    ]
