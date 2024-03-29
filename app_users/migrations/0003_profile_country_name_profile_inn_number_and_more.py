# Generated by Django 4.1.6 on 2023-02-14 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_profile_bio_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='inn_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='passport_number',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tel_number',
            field=models.IntegerField(blank=True, max_length=9, null=True, unique=True),
        ),
    ]
