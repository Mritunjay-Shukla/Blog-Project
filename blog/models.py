from django.db import models
from django.utils.text import slugify
from account.models import Profile
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default=None)

    def __str__(self):
        return self.name



        
class Post(models.Model):
    statuses = [("D","Draft"),("P","Published")]

    title = models.CharField(max_length = 250)
    #content = models.TextField()
    content = RichTextField(blank=True, null=True)
    status = models.CharField(max_length=1,choices=statuses,default="D")
    image = models.ImageField(upload_to = "blog/", blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique= True, blank= True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    
    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('post-detail', args=[self.slug])


