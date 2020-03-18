from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

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








