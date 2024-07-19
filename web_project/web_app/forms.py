from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    email = forms.EmailField()
    
class meta:
    model=User
    fields=['username','fname','lname','email','password1','password2']