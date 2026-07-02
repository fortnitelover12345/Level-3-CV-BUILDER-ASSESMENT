from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    return redirect('/') 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def create_cv_view(request):
   
    return redirect('template_gallery') 

@login_required
def upload_cv_view(request):

    return render(request, 'upload_cv.html')
