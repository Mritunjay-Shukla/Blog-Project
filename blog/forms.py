from django import forms
from blog.models import Category, Post
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
class Contactus(forms.Form):
    name = forms.CharField(widget= forms.TextInput(attrs= {'class':'contactformname1'}), max_length=30, label="Your Name")
    email = forms.EmailField(required=False, widget= forms.TextInput(attrs= {'class':'contactformname1'}))
    phone = forms.RegexField(regex="^[6-9]\d{9}$", required=False,widget= forms.TextInput(attrs= {'class':'contactformname1'}))
    message = forms.CharField(widget = forms.Textarea(attrs= {'class':'contactformname'}))
   

    def clean(self):
        cleaned_data = super().clean()
        if not(cleaned_data.get("email") or cleaned_data.get("phone")):
            raise forms.ValidationError("Please fill at least one!",code="invalid")
        elif self.cleaned_data["email"]:
            data = self.cleaned_data["email"]
            if "gmail" not in data:
                raise forms.ValidationError("can't match email",code="invalid")
   
      
class Registration(forms.Form):
        username = forms.CharField(widget= forms.TextInput(attrs= {'class':'contactformname1'}), max_length=100)
        email = forms.EmailField()
        password = forms.CharField(max_length=30, min_length=8)
        re_password = forms.CharField()



        def clean(self):
                cleaned_data = super().clean()
                password = cleaned_data.get("password")
                re_password = cleaned_data.get("re_password")
                if password != re_password:
                    raise forms.ValidationError("missmatch", code="invalid")

    

#class Postform(forms.Form):
 #       statuses = [("D","Draft"),("P","Published")]
  #      title = forms.CharField(max_length = 250)
   #     content = forms.CharField(widget = SummernoteWidget)
    #    status = forms.ChoiceField(choices= statuses)
     #   image = forms.ImageField(required= False)
      #  category = forms.ModelChoiceField(queryset = Category.objects.all())

#class Postform(forms.ModelForm):
 #   class Meta:
  #      model = Post
   #     fields = ('title', 'content', 'status', 'image', 'category)

    #    widgets = {
     #       'title': forms.TextInput(attrs={'class':'form-controle'}),
      #      'content': forms.TextInput(attrs={'class':'form-controle'}),
       #     'status': forms.TextInput(attrs={'class':'form-controle'}),
        #    'category': forms.TextInput(attrs={'class':'form-controle'}),
        #}



class Pstform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "status", "image", "category"]

        widgets = {
        'title': forms.TextInput(attrs={'class':'contactformname2'}),
        'content': forms.Textarea(attrs={'class':'contactformname2'}),
        'status': forms.Select(attrs={'class':'contactformname2'}),
        'category': forms.Select(attrs={'class':'contactformname2'}),
        
        }
       

    def clean_title(self):
            title = self.cleaned_data.get('title')
            slug = slugify(title)
            try:
                post_obj = Post.objects.get(slug = slug)
                raise forms.ValidationError("Title is already exists",code="Invalid")
            except ObjectDoesNotExist:
                return title

