# Generated by Django 4.0.6 on 2022-08-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='current_salary',
        ),
        migrations.AddField(
            model_name='company',
            name='establishment_date',
            field=models.IntegerField(default=None),
        ),
    ]