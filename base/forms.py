from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import SetPasswordForm as SetPassword
from django.contrib.auth import password_validation
from django import forms

from .models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email',
        ]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]


class CustomSetPasswordForm(forms.Form):
    new_password1 = forms.CharField(
       label='Nova senha',
       widget=forms.PasswordInput(),
    )
    new_password2 = forms.CharField(
       label='Confirmar senha',
       widget=forms.PasswordInput(),
    )

    def compara_senhas(self):
        if self.new_password1 != self.new_password2:
            return False
        else:
            return True



