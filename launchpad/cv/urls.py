from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('templates/', views.templates, name='templates'),
        path('overview/', views.overview, name='overview'),
        path('edit/', views.edit_profile, name='edit_profile'),
        path('cv/<int:profile_id>/', views.overview, name='cv_template'),
    ]