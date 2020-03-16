from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView

from .forms import UserCreationFormCustom
from .models import User


class CadastroView(CreateView):
    model = User
    form_class = UserCreationFormCustom
    success_url = reverse_lazy('index')
    template_name = 'registration/register.html'

cadastro = CadastroView.as_view()


class IndexView(TemplateView):
    template_name = 'base/index.html'

index = login_required(IndexView.as_view())

class CustomResetPassordView(PasswordResetView):
    email_template_name = 'registration/custom_password_reset_email.html'
    subject_template_name = 'registration/custom_password_reset_subject.txt'
    template_name = 'registration/custom_password_reset_form.html'
    success_url = reverse_lazy('login')

reset_senha = CustomResetPassordView.as_view()

class CustomPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'registration/custom_password_reset_confirm.html'
    success_url = reverse_lazy('login')

reset_confirm_senha = CustomPasswordConfirmView.as_view()


