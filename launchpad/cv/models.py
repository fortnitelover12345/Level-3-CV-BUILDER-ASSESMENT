from django.db import models
from django.db import models

class CVProfile(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    summary = models.TextField()
    experience = models.TextField(help_text="Separate roles with new lines or use JSON")
    education = models.TextField()
    skills = models.CharField(max_length=255, help_text="Comma-separated skills")

    def __str__(self):
        return self.full_name

# Create your models here.
 
 