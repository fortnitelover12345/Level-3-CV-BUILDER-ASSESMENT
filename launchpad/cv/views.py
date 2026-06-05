from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import CVProfile

# Create your views here.
def templates(request):
    #return HttpResponse("This is the template page.")
    return render(request, 'cv/templates.html')

def overview(request): 
    return render(request, 'cv/overview.html')

@login_required
def edit_profile(request):
    # Fetch existing profile or create a blank one for this user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('cv_view')  # Redirect to the CV template page
    else:
        form = ProfileForm(instance=profile)
        
    return render(request, 'gather_info.html', {'form': form})

@login_required
def overview(request, profile_id):
    # This securely fetches the specific profile requested by the URL structure
    profile = get_object_or_404(CVProfile, id=profile_id, user=request.user)
    
    context = {
        'profile': profile,
    }
    return render(request, 'cv_template.html', context)