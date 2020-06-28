from django.contrib import admin
from django.urls import path, include
from blog.views import HomePage, post_details, categ, category_post_details, Contact, Postform, register_form, Postupform, post_delete_form
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [

    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    
    
    
   