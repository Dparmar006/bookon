# Generated by Django 3.1.2 on 2020-12-06 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('district', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=50)),
                ('like', models.IntegerField(blank=True, null=True)),
                ('averageServiceTime', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
