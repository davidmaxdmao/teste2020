from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import logout
from django.core.mail import send_mail

from django.conf import settings
from .forms import LoginForm
from .forms import UserForm
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
        return render(request, 'registration/register.html', {'form': form})


def password_reset_view(request):
    mensagem = '''
        Ola!
        Para iniciar o processo de redefinição de senha para sua conta {{ user.get_username }} do TesteSite ,click no link a baixo.
        http://127.0.0.1:8000/login/
    '''
    if request.method == 'POST':
        form = UserForm(request.POST)
        send_mail(
            'Teste2020 Recuperação de senha',
            mensagem,
            settings.EMAIL_HOST_USER,
            [request.POST['email']],
            fail_silently=False,
        )
        return redirect('login')
    elif request.method == 'GET':
        form = UserForm()
        return render(request, 'registration/custom_password_reset_form.html', {'form': form})








