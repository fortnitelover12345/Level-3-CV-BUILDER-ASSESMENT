from django.contrib import admin
from cv.models import CVProfile

@admin.register(CVProfile)
class CVProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'experience')  
    search_fields = ('full_name', 'email')          