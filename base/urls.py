from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls


from .views import login_view
from .views import logout_view
from .views import index_view
from .views import register_view

urlpatterns = [
    path('index/', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    # path('register/', cadastro, name='register'),
    # path('index/', index, name='index'),
    # path('reset-senha/', reset_senha, name='PasswordReset'),
    # path('reset/<uidb64>/<token>/', reset_confirm_senha, name='reset_confirm_senha'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('reste-done/', reset_done, name='password_reset_done'),
    # path('change-done/', custom_password_change_done, name='custom_password_change_done'),
]