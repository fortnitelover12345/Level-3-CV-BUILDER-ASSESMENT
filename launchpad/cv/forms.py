# forms.py
import re
from django import forms
from .models import CVProfile
  # Fields the user needs to fill out for their CV
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CVProfile
        fields = ['full_name', 'phone', 'summary', 'skills', 'experience', 'education']

    def clean_phone(self):

        phone_input = self.cleaned_data.get('phone')
        
        clean_number = re.sub(r'[\s\-()+\.]', '', phone_input)

        if not clean_number.isdigit() or not (7 <= len(clean_number) <= 13):
            raise forms.ValidationError("Please enter a valid phone number (e.g., 021 000 000 or 07 578 0000).")
        return phone_input

    def clean_summary(self):
        summary_text = self.cleaned_data.get('summary').strip()
        
        if len(summary_text) < 15:
            raise forms.ValidationError("Your professional summary should be at least a full sentence (minimum 15 characters).")
            
        return summary_text

    def clean_experience(self):
        exp_text = self.cleaned_data.get('experience').strip()
        
        if len(exp_text) < 10:
            raise forms.ValidationError("Please provide a real description of your work history.")
            
        return exp_text