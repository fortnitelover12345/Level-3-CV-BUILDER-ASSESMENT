from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")  

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  