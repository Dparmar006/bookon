# Generated by Django 3.1.4 on 2020-12-08 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customermore_ownermore'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermore',
            name='customer_username',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='users.customer'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OwnerMore',
        ),
    ]
