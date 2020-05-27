from django.contrib.auth import login
from django.http import Http404
from django.shortcuts import render, redirect

# from .models import User
from .forms import RegistrationForm, VerificationForm


def verify(request):
    user = request.user
    if request.method == 'GET':
        form = VerificationForm()
        return render(request, 'account/register_success.html', context={'form': form})
    elif request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            if user.secret_token_valid(form.data['token']):
                user.user_verify()
                return redirect('/')
    else:
        return Http404()


def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'account/register.html', context={'form': form})
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.send_token()
            login(request, user)
            form = VerificationForm()
            return render(request, 'account/register_success.html', context={'form': form})
        else:
            return render(request, 'account/register.html', context={'form': form})
