# models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 

class CVProfile(models.Model):
    # Links profile directly to the logged-in user
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    summary = models.TextField(blank=True)
    skills = models.TextField(help_text="Comma-separated skills", blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)


# Create your models here.
 
 