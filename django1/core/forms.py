from django import forms
from .models import Applicationuser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class User_form(UserCreationForm):
     class Meta:
         model = User
         fields =  ('username','password1','password2')
         labels ={
            'username' : "Enter Unique username",
            'password1':"Enter password",
            'password2':  "Conform password"
        }
         

class App_user_form(forms.ModelForm):
    class Meta:
        model = Applicationuser
        fields = '__all__'
        exclude= ('uid','user')
        labels ={
            'user_satus' :'Select UserType',
            'phonenumber' : "Enter Phone Number",
            'profile_pic':"Select Profilepicture",
            'address':  "Enter Address"
        }