from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegisterForm


def register(request):
    # validating that we are getting a post response from http
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created, you now may log in as {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required  # decorator to require a logged in user to see the profile.html so when trying to access
# the profile page directly without being logged in, it would ask to log in and redirect to profile after
def profile(request):
    return render(request, 'users/profile.html')
