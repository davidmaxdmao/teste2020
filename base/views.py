from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import LoginView

from .forms import UserCreationFormCustom
from .models import User


class CustomLoginView(LoginView):
    def form_valid(self, form):
        self.request.session['recuperar_senha'] = False
        return super().form_valid(form)
    
login = CustomLoginView.as_view()

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

    # Mostra na sessão se o usuario iniciou o processo de recuperar senha,
    # deste modo na pagina de login pode ser exibida uma mensagem de orientação
    # de acordo com o valor guardado na sessão
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['recuperar_senha'] = True
        return context

reset_senha = CustomResetPassordView.as_view()



class CustomPasswordResetDoneView(TemplateView):
    template_name = 'registration/custom_password_reset_done.html'

reset_done = CustomPasswordResetDoneView.as_view()


class CustomPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'registration/custom_password_reset_confirm.html'
    success_url = reverse_lazy('custom_password_change_done')

reset_confirm_senha = CustomPasswordConfirmView.as_view()


class CustomPasswordChangeDoneView(TemplateView):
    template_name = 'registration/custom_password_change_done.html'

    # Depois que o usuário recuperou a senha, seta o valor de
    # 'reuperar_senha', a sessão, para False, para assim a mensagem
    # de orientação n ser mais exibida na página de login
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['recuperar_senha'] = False
        return context

custom_password_change_done = CustomPasswordChangeDoneView.as_view()


