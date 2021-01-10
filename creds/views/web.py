from django.shortcuts import render
from creds.forms import CreateUserForm


def login(request):
    return render(request, 'creds/login.html')


def signup(request):
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'creds/signup.html', context)


def reset_password(request):
    return render(request, 'creds/reset-password.html')
