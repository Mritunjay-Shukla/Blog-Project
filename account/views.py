from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from account.forms import SignupForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.views import generic
from blog.models import Post
from account.models import Profile
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from account.forms import Profileform
# Create your views here.

class Signup(CreateView):
    model = User  
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        to_return = super().form_valid(form)
        login(self.request, self.object)
        return to_return
  
   
class Profileupdate(generic.UpdateView):
    model = Profile 
    fields = ['pic', 'bio']
    template_name = 'registration/profile_update.html'
    success_url = '/userdetail'

def profupadte(request, slug):
    profile = Profile.objects.get(slug = slug)
    if request.method == 'GET':
        form = Profileform(instance = profile)
        return render(request, "registration/profile_update.html", context = {"form":form})
    else:
        print(request.FILES)
        form = Profileform(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/userdetail')

    #def form_valid(self, form):
     #   form.save()
      #  LoginView(username="self.username", password="self.password")
       # return super().form_valid(form)

def Userdetailpage(request):
    posts = Post.objects.filter(author = request.user.profile)   
    profile = Profile.objects.get(user_id = request.user.id) 
    print(profile)
    return render(request, "registration/user.html",context = {"posts":posts, "profile":profile})
