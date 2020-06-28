"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import HomePage, post_details, categ, search, category_post_details, contactus, Contact, Postform, register_form, Postupform, post_delete_form
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from account.views import Signup, Userdetailpage, Profileupdate, profupadte


urlpatterns = [
    path('account/', include('account.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('blogs/<slug:slug>', post_details, name='post-detail'),
    path('search/blogs/<slug:slug>', post_details),
    path('profup/<slug:slug>', profupadte),
    path("blogs/account/logout",LogoutView.as_view()),
    path("registration/login",LoginView.as_view()),
    path("blogs/account/login",LoginView.as_view(template_name="account/login.html")),
    path("category/blogs/account/logout",LogoutView.as_view()),
    path("category/blogs/account/login",LoginView.as_view(template_name="account/login.html")),
    path("category/account/logout",LogoutView.as_view()),
    path("category/account/login",LoginView.as_view(template_name="account/login.html")),
    path('category/blogs/<int:id>', category_post_details),
    path('category/<str:category>', categ),
    path('search/', search, name='searchbar'),
    path('contact', Contact.as_view()),
    path('account/help', contactus),
    path('post', Postform.as_view()),
    path('post/<int:pk>', Postupform.as_view()),
    path('delete/<int:id>', post_delete_form),
    path("account/register", Signup.as_view()),
    path("account/account/login",LoginView.as_view(template_name="registration/login.html")),
    path("login",LoginView.as_view(template_name="account/login.html")),
    #path('register', register_form),
    path("userdetail", Userdetailpage),
    path('profileupdate/<int:pk>', Profileupdate.as_view()),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 