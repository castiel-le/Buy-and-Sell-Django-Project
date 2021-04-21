from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    # validating that we are getting a post response from http
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # TODO 29:49
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})