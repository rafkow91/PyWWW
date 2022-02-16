from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm


def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            permission = Permission.objects.get(name='Can add tag')
            user.user_permissions.add(permission)
        return redirect('/')
    else:
        form = RegisterForm()
    return render(response, 'accounts/register.html', {'form': form})


def login(response):
    if response.method == 'POST':
        form = LoginForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = LoginForm()
    return render(response, 'login.html', {'form': form})
