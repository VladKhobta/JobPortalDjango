# Generated by Django 4.1 on 2022-09-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(error_messages={'required': 'Oh no'}, max_length=20, unique=True, verbose_name='Phone number'),
        ),
    ]
