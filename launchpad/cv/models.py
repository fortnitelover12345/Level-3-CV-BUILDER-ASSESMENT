# models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 
from django.db.models.signals import post_save 
from django.dispatch import receiver

class CVProfile(models.Model):
    # Links profile directly to the logged-in user
    full_name = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    summary = models.TextField(blank=True)
    skills = models.TextField(help_text="Comma-separated skills", blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    
    TEMPLATE_CHOICES = [
        ('template1', 'Modern Green'),
        ('template2', 'Classic Slate'),
        ('template3', 'Creative Teal'),
        ('template4', 'Minimal Elegant'),
        ('template5', 'Executive Charcoal'),
        ('template6', 'Warm Ochre'),
        ('template7', 'Rose Wine'),
        ('template8', 'Royal Blue'),
        ('template9', 'Dark Mode'),
        ('template10', 'Minimal Stack'),
        ('template11', 'Forest Compact'),
        ('template12', 'Amber Clean'),
    ]

    design_choice = models.CharField(max_length=20, choices=TEMPLATE_CHOICES, default='template1')


def __str__(self):
        return f"{self.user.email}'s Profile"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_cv_profile(sender, instance, created, **kwargs):
 
    if created:
        CVProfile.objects.create(user=instance)

# Create your models here.
 
 