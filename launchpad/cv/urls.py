from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.template_gallery, name='template_gallery'),
    path('templates/preview/<str:template_name>/', views.preview_template, name='preview_template'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('<int:profile_id>/', views.overview, name='cv_template'),
]