from django.shortcuts import render
from creds.forms import (
    CreateUserForm, UserPassResetForm, UserLoginForm
)


def login(request):
    form = UserLoginForm()
    context = {'form': form}
    return render(request, 'creds/login.html', context)


def signup(request):
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'creds/signup.html', context)


def reset_password(request):
    form = UserPassResetForm()
    context = {'form': form}
    return render(request, 'creds/reset-password.html', context)
