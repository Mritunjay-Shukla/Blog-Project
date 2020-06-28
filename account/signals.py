from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import User
from django.models import Profile

@receiver(post_save,sender = User)
def create_profile(sender, instance, created, **kwargs):
    #print(sender, kwargs)
    #if created:
     #   Profile.objects.create(user= instance)

