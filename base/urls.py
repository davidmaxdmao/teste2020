from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls

from .views import cadastro
from .views import index
from .views import reset_senha
from .views import reset_confirm_senha
from .views import reset_done
from .views import custom_password_change_done
from .views import login
from .views import reset_password


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', cadastro, name='register'),
    path('index/', index, name='index'),
    path('reset-senha/', reset_senha, name='PasswordReset'),
    path('reset/<uidb64>/<token>/', reset_confirm_senha, name='reset_confirm_senha'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reste-done/', reset_done, name='password_reset_done'),
    path('change-done/', custom_password_change_done, name='custom_password_change_done'),
    path('resete-password', reset_password, name='resete_password'),
]