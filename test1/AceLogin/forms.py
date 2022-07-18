from django. forms import ModelFormfrom
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms 
from .models import RegisterUser

class Register(UserChangeForm):
    class Meta:
        model= RegisterUser
        fields=['firstName','lastName','title','phoneNumber','email','password',]