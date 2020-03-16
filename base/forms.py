from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserCreationFormCustom(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
        ]