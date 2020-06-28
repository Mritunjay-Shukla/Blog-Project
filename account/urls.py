from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account.views import Signup
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   
   path("", include("django.contrib.auth.urls")),
   path("login",LoginView.as_view(template_name="account/login.html")),
   path("account/account/login",LoginView.as_view(template_name="account/login.html")),
  # path("blogs/account/logout",LogoutView.as_view()),
   path("account/register", Signup.as_view()),

] 
