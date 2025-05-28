from django.shortcuts import render
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.conf import settings

from django.contrib.auth import views as auth_views
from django.views.generic import CreateView
from django.views import View

from .forms import UserCreationForm, LoginForm, PasswordResetForm
from .models import User
from .tokens import ActivationToken


activation_token = ActivationToken()

def send_activation_email(request, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = activation_token.make_token(user)
    activation_link = request.build_absolute_uri(
            reverse('account:account_activate', kwargs={'uidb64': uid, 'token': token})
        )
    
    send_mail(
            'Ative sua conta',
            f'Clique no link para ativar sua conta: {activation_link}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False
        )


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy('account:register_success')

    def form_valid(self, form):
        user = form.save()
        send_activation_email(self.request, user)

        return super().form_valid(form)


class RegisterSuccessView(View):
    def get(self, request):
        return render(request, 'account_comp/register_success_comp/register_success.html')


class LoginView(auth_views.LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('account:register')


class LogouView(auth_views.LogoutView):
    next_page = reverse_lazy('account:login')


class ActivationAccountView(View):
    def get(self, request, uidb64, token):
        user =  self.get_user_from_uid(uidb64)

        if user is None:
            messages.error(request, 'Link de ativação inválido ou expirado. Clique abaixo para solicitar um novo link.')
            return render(request, 'account_comp/activation_comp/activation_invalid.html')

        elif user.is_active:
            messages.warning(request, 'Parece que sua conta já está ativa. Por favor, efetue o login.')
            return render(request, 'account_comp/activation_comp/activation_invalid.html')

        elif activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Sua conta foi ativada com sucesso! Faça login para continuar.')
            return render(request,'account_comp/activation_comp/activation_success.html')

        else:
            messages.error(request, 'Link de ativação inválido ou expirado. Clique abaixo para solicitar um novo link.')
            return render(request, 'account_comp/activation_comp/activation_success.html')

    def get_user_from_uid(self, uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            return User.objects.get(pk=uid)
        
        except (User.DoesNotExist, ValueError, TypeError, UnicodeDecodeError):
            return None
        

class PasswordResetView(auth_views.PasswordResetView):
    form_class = PasswordResetForm
    email_template_name = 'account_comp/password_reset_comp/password_reset_email.html'
    template_name = 'account_comp/password_reset_comp/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_done')


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'account_comp/password_reset_comp/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'account_comp/password_reset_comp/password_reset_confirm.html'
    success_url = reverse_lazy("account:password_reset_complete")


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'account_comp/password_reset_comp/password_reset_complete.html'