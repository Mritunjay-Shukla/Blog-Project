from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from account.models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'contactformname2'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'contactformname2'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'contactformname2'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')
        widgets = {
        'username':forms.TextInput(attrs= {'class':'contactformname2'}),
        'last_name':forms.TextInput(attrs= {'class':'contactformname2'}),
        'first_name':forms.TextInput(attrs= {'class':'contactformname2'}),   
        } 

class Profileform(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['pic', 'bio']

        

   
