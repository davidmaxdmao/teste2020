from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
#from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm as CustomPasswordForm
from django.contrib.auth import logout
from django.core.mail import send_mail

from django.conf import settings
from .forms import LoginForm
from .forms import UserForm
from .forms import CustomSetPasswordForm
from .models import User


@login_required
def index_view(request):
    return render(request, 'base/index.html', {})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    elif request.method == "GET":
        form = LoginForm()
        return render(request, 'registration/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    elif request.method == 'GET':
        form = UserForm()
        return render(
            request,
            'registration/register.html',
            {'form': form}
        )


def password_reset_view(request):
    email_template_name = 'registration/custom_password_reset_email.html'
    subject_template_name = 'registration/custom_password_reset_subject.txt'
    token_generator = default_token_generator

    if request.method == 'POST':
        form = CustomPasswordForm(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
            }
            form.save(**opts)
        return redirect('login')
    elif request.method == 'GET':
        form = CustomPasswordForm()
        return render(
            request,
            'registration/custom_password_reset_form.html',
            {'form': form}
        )


def reset_confirm_senha(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        form = CustomSetPasswordForm(request.POST)
        if form.is_valid():
            form.new_password1 = request.POST['new_password1']
            form.new_password2 = request.POST['new_password2']
            if form.compara_senhas():
                print('senha iguais')
                user.set_password(form.new_password1)
                user.save()
                return redirect('login')
    elif request.method == "GET":
        form = CustomSetPasswordForm()
        return render(
            request,
            'registration/custom_password_reset_confirm.html',
            {'form': form}
       )







