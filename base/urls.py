from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls

from .views import cadastro
from .views import index
from .views import reset_senha
from .views import reset_confirm_senha


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', cadastro, name='register'),
    path('index/', index, name='index'),
    path('reset-senha/', reset_senha, name='PasswordReset'),
    path('reset/<uidb64>/<token>/', reset_confirm_senha, name='reset_confirm_senha'),
    path('accounts/', include('django.contrib.auth.urls')),
]