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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        message1 = 'Enviámos-lhe instruções por e-mail para definir sua senha,' \
                   'se houver uma conta com o e-mail digitado. Você deve recebê-las em breve.'
        message2 = 'Se você não receber um e-mail, verifique se inseriu o endereço com ' \
                   'o qual se registrou e verifique sua pasta de spam.'
        context['message1'] = message1
        context['message2'] = message2
        return context

reset_senha = CustomResetPassordView.as_view()

class CustomPasswordResetDoneView(TemplateView):
    template_name = 'registration/custom_password_reset_done.html'

reset_done = CustomPasswordResetDoneView.as_view()


class CustomPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'registration/custom_password_reset_confirm.html'
    success_url = reverse_lazy('password_change_done')

reset_confirm_senha = CustomPasswordConfirmView.as_view()


class CustomPasswordChangeDoneView(TemplateView):
    template_name = 'registration/custom_password_change_done.html'

password_change_done = CustomPasswordChangeDoneView.as_view()


