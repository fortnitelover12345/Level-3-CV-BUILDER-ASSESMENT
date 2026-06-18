from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import CVProfile

def templates(request):
    return render(request, 'cv/templates.html')

@login_required
def edit_profile(request):
    profile = request.user.cvprofile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('cv_template', profile_id=profile.id) 
    else:
        form = ProfileForm(instance=profile)
        
    return render(request, 'cv/gather_info.html', {'form': form})

@login_required
def overview(request, profile_id):
    profile = get_object_or_404(CVProfile, id=profile_id, user=request.user)
    
    context = {
        'profile': profile,
    }
    return render(request, 'cv/cv_template.html', context)

@login_required
def cv_preview(request):
    profile = request.user.cvprofile
    return render(request, 'cv/cv_template.html', {'profile': profile})
@login_required
def template_gallery(request):
    return render(request, 'cv/template.html')

@login_required
def preview_template(request, template_name):

    profile = request.user.cvprofile
    if request.method == 'POST':
        profile.design_choice = template_name
        profile.save()
        return redirect('edit_profile')
        
   
    return render(request, 'cv/preview_template.html', {
        'profile': profile, 
        'preview_mode': True,
        'selected_template': template_name
    })

@login_required
def edit_profile(request):
    profile = request.user.cvprofile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('cv_template', profile_id=profile.id)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'cv/gather_info.html', {'form': form})