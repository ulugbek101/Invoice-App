# Generated by Django 4.1.6 on 2023-02-14 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_profile_country_name_profile_inn_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tel_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
