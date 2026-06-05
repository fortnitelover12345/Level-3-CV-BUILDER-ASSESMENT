# forms.py
from django import forms
from .models import CVProfile
  # Fields the user needs to fill out for their CV
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CVProfile
        fields = ['phone', 'summary', 'skills', 'experience', 'education']
