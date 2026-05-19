from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Import your custom User model
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")

    class Meta:
        model = User  # Use your custom User model
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Check if the email domain is valid
        allowed_domains = ['example.com', 'mydomain.com']
        domain = email.split('@')[-1]
        if domain not in allowed_domains:
            raise ValidationError("Please use an email address with a valid domain (e.g., example.com).")

        # Check if the email is already in use
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use. Please use a different email.")

        return email