# Generated by Django 3.2.5 on 2023-02-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0004_alter_profile_tel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='profiles/user-default.png', null=True, upload_to='profiles/'),
        ),
    ]