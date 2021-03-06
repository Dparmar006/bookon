# Generated by Django 3.1.4 on 2021-05-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201209_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerMore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_start_time', models.DateTimeField(blank=True, null=True)),
                ('service_end_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='bookonuser',
            name='type',
            field=models.CharField(choices=[('OWNER', 'Owner'), ('CUSTOMER', 'Customer')], default='CUSTOMER', max_length=20),
        ),
    ]
