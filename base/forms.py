from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserCreationFormCustom(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]