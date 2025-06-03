from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from .forms import LoginForm, PasswordResetForm


class LoginView(auth_views.LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('dashboard')


class LogouView(auth_views.LogoutView):
    next_page = reverse_lazy('account:login')
        

class PasswordResetView(auth_views.PasswordResetView):
    form_class = PasswordResetForm
    email_template_name = 'account_includes/password_reset_includes/password_reset_email.html'
    template_name = 'account_includes/password_reset_includes/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_done')


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'account_includes/password_reset_includes/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'account_includes/password_reset_includes/password_reset_confirm.html'
    success_url = reverse_lazy("account:password_reset_complete")


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'account_includes/password_reset_includes/password_reset_complete.html'