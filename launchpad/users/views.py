from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            return redirect('login')  # Redirect to login page after successful sign-up
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    return redirect('/') 