from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post, Category
from blog.forms import Contactus, Registration, Pstform
from django.views import View
from django.views import generic
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from account.models import Profile
from django.db.models import Q
#from blog.forms import Registration
# Create your views here. 

#class index(View):
 #  def get(self, request):
  #      posts = Post.objects.all()
   #     category = Category.objects.all()     
    #    return render(request, "stories.html",context = {"posts":posts, "category":category})

class HomePage(generic.ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.filter(status='P')
    template_name = "stories.html"
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


@login_required(login_url = '/registration/login')
def post_details(request, slug):
    post = Post.objects.get(slug = slug)
    profile = Profile.objects.get(user_id = request.user.id)
    return render(request, "blog-post.html", context = {"post":post, "profile":profile})

#class post_details(generic.DetailView):
 #   model = Post
   # queryset = Post.objects.filter(status = 'P')
    #template_name = 'blog-post.html'

    

@login_required(login_url = '/registration/login')
def category_post_details(request, id):
    post = Post.objects.get(id = id)
    profile = Profile.objects.get(user_id = request.user.id)
    return render(request, "category_blog_post.html", context = {"post":post, "profile":profile})

def categ(request, category):
    post = Post.objects.filter(category = category, status= 'P')
    return render(request, "cat.html", context={"post":post})

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        posts = Post.objects.filter(
        Q(title__icontains = search, status='P')|
        Q(content__icontains = search, status='P')
        #Q(author__first_name = search, status='P')
        )
        return render(request, "stories2.html", context={'posts':posts})

#class contact_form(View):
 #   def get(self, request):
  #      form = Contactus()
   #     return render(request, "contactform.html", context = {"form":form})
    #def post(self, request):
     #   form = Contactus(request.POST)
      #  if form.is_valid(): 
       #     print(form.cleaned_data)
        #    return HttpResponse("<h1>Thanks!!</h1>")
        #else:
         #   print(form.errors)
          #  return render(request, "contactform.html", context = {"form":form})


class Contact(FormView):
    form_class = Contactus
    success_url = 'account/help'
    template_name = 'contactform.html'

    def form_valid(self, form):
        return super().form_valid(form)

def contactus(request): 
    return render(request, 'succcontact.html')

#class post_form(View): 
#
 #   def get(self, request):
  #      form = Postform()
   #     return render(request, "post_form.html", context = {"form":form})
    #def post(self, request):
     #   print(request.FILES)
      #  form = Postform(request.POST, request.FILES)
       # if form.is_valid(): 
        #    form.save()
         #   return HttpResponse("<h1>Thanks!!</h1>")
        #else:
         #   print(form.errors)
          #  return render(request, "post_form.html", context = {"form":form})


class Postform(LoginRequiredMixin,PermissionRequiredMixin,generic.CreateView):
    permission_required = 'blog.add_post'
    model = Post
    form_class = Pstform
    success_url = '/'
    template_name = 'post_form.html'
    login_url = 'registration/login'
    

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

#def post_update_form(request,id):  
 #   post = Post.objects.get(id = id)
  #  if request.method == "GET":
   #     form = Postform(instance = post)
    #    return render(request, "post_form.html", context = {"form":form})
    #else:
     #   form = Postform(request.POST, request.FILES, instance=post)
      #  if form.is_valid(): 
       #     form.save()
        #    return HttpResponse("<h1>Thanks!!</h1>")
        #else:
         #   print(form.errors)
          #  return render(request, "post_form.html", context = {"form":form})

class Postupform(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    permission_required = 'blog.change_post'
    model = Post
    fields = ["title", "content", "status", "image", "category"]
    #success_url = reverse_lazy('post-detail')
    template_name = 'post_form.html'
    login_url = 'registration/login'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def test_func(self, *args, **kwargs):
        print(self.request.GET)
        print(self.kwargs.get('pk'))
        post = Post.objects.get(pk = self.kwargs.get('pk'))
        if post.author == self.request.user.profile:
            return True
        else:
            return False

   

            

def post_delete_form(request,id):
    if request.method == 'GET':
        return render(request, "delete.html")
    else:
        post = Post.objects.get(id = id)
        post.delete()
        return redirect('/userdetail')


def register_form(request):
    if request.method == "GET":
        form = Registration()
        return render(request, "signup.html", context = {"form":form})
    else:
        form = Registration(request.POST)
        if form.is_valid(): 
            print(form.cleaned_data)
            return HttpResponse("<h1>Thanks for signup!!</h1>")
        else:
            print(form.errors)
            return render(request, "signup.html", context = {"form":form})








