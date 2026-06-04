from django.shortcuts import render, get_object_or_404
from .models import CVProfile 

# Create your views here.
def templates(request):
    #return HttpResponse("This is the template page.")
    return render(request, 'cv/templates.html')

def overview(request): 
    return render(request, 'cv/overview.html')

def cv_view(request, profile_id):
    profile = get_object_or_404(CVProfile, pk=profile_id)
    skills_list = [skill.strip() for skill in profile.skills.split(',')]
    context = {
    'profile': profile,
    'skills': skills_list
    }
    return render(request, 'cv_template.html', context)