# Generated by Django 4.0.6 on 2022-08-15 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_type_delete_usertype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='type',
            new_name='user_type',
        ),
    ]