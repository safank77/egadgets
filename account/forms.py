from django import forms
from django.contrib .auth.forms import UserCreationForm
from django.contrib .auth.models import User 





class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)

class Regform(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
            