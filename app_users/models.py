import uuid
import datetime

from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='profiles/', default='profiles/user-default.png', null=True)
    country_name = models.CharField(max_length=255, blank=True, null=True)
    passport_number = models.CharField(max_length=9, blank=True, null=True)
    inn_number = models.IntegerField(null=True, blank=True)
    tel_number = models.IntegerField(null=True, blank=True, unique=True)

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.fullname}'  # admin - Mahmudjon
