# Generated by Django 4.1.6 on 2023-02-06 18:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_users', '0002_profile_bio_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('amount', models.BigIntegerField(default=10000000)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owner_invoices', to='app_users.profile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sender_invoices', to='app_users.profile')),
            ],
        ),
    ]
