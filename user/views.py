from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm


@login_required()
def profile_view(request):
    return render(request, 'user/profile_user.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            user = authenticate(username=user.username, password=password)
            if user:
                login(request, user)
                return redirect('profile_url')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
