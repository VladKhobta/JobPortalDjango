# Generated by Django 4.0.6 on 2022-08-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_establishment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='designation',
            field=models.CharField(default='Vaya', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
