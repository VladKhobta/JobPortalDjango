# Generated by Django 4.0.6 on 2022-08-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_type_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=12391293, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]