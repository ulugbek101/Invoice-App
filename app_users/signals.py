from django.db.models.signals import post_delete, post_save

from .models import Profile
from django.contrib.auth.models import User

def user_delete_on_profile_delete(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


def profile_create_on_user_create(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            fullname=f'{instance.first_name} {instance.last_name}' if instance.first_name and instance.last_name else '',
            email=instance.email
        )
        profile.save()


post_delete.connect(receiver=user_delete_on_profile_delete, sender=Profile)
post_save.connect(receiver=profile_create_on_user_create, sender=User)


