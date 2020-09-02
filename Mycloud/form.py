from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=21, required=True, help_text='first name')
    last_name = forms.CharField(max_length=21, required=True, help_text='last name')
    email = forms.EmailField(max_length=254, help_text='Requied, input a valid email address')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=21, required=True)
    password = forms.PasswordInput()
    model = User
    field =('username', 'password', )


