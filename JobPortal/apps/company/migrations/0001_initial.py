# Generated by Django 4.0.6 on 2022-08-16 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_rename_type_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('designation', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.CharField(blank=True, max_length=254, null=True)),
                ('current_salary', models.IntegerField(default=0)),
                ('website_url', models.URLField(max_length=254)),
            ],
        ),
    ]
