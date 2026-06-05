# G:\My Drive\L3DTSD\Level 3 CV BUILDER ASSESMENT\launchpad\cv\admin.py
from django.contrib import admin
from cv.models import CVProfile

@admin.register(CVProfile)
class CVProfileAdmin(admin.ModelAdmin):
    # We will display the profile database ID and the account owner's email address
    list_display = ('id', 'get_email', 'phone', 'experience')  
    search_fields = ('user__email', 'phone') 

    # This pulls the email address directly from the custom user model safely
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'User Email'
