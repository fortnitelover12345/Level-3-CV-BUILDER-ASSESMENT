from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('templates/', views.templates, name='templates'),
        path('overview/', views.overview, name='overview'),
        path('cv/<int:profile_id>/', views.cv_view, name='cv_template'),
    ]