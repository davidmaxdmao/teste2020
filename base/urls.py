from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls

from .views import login_view
from .views import logout_view
from .views import index_view
from .views import register_view
from .views import password_reset_view
from .views import reset_confirm_senha

urlpatterns = [
    path('index/', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('reset-password/', password_reset_view, name='reset_password'),
    path('set-password/<int:pk>/', reset_confirm_senha, name='set_password'),
]