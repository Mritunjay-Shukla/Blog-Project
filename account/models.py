from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.text import slugify
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="account/", blank=True)
    bio = models.TextField(blank=True)
    #first_name = models.CharField(max_length=50, blank= True)
    #last_name = models.CharField(max_length=50, blank= True)
    slug = models.SlugField(blank= True)

    def __str__(self): 
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super().save(*args, **kwargs)

@receiver(post_save,sender = User)
def create_profile(sender, instance, created, **kwargs):
     print(sender, kwargs)
     if created:
        Profile.objects.create(user= instance)

@receiver(post_save, sender= get_user_model())
def assign_default_group(sender, instance, created, **kwargs):
    if created:
        reader = Group.objects.get(name = 'reader')
        instance.groups.add(reader)



