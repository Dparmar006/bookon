# Generated by Django 3.1.4 on 2020-12-14 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20201208_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='shop_description',
        ),
        migrations.RemoveField(
            model_name='service',
            name='shop_name',
        ),
    ]