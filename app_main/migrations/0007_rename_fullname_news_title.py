# Generated by Django 3.2.5 on 2023-02-19 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0006_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='fullname',
            new_name='title',
        ),
    ]
