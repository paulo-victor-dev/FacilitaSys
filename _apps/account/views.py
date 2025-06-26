from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, View
from django.db.models import Q, Value, F
from django.db.models.functions import Concat
from django.http import HttpResponse

import io, pandas as pd

from .forms import LoginForm, PasswordResetForm
from .models import User


class LoginView(auth_views.LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('account:login')


class UsersListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = User.objects.annotate(
            full_name=Concat(
                F('first_name'),
                Value(' '),
                F('last_name')
            )
        )

        search = self.request.GET.get('search')
        search_filter = self.request.GET.get('filter')

        if search and search_filter:
            lookup = f'{search_filter}__icontains'

            queryset = queryset.filter(
                Q(**{lookup: search})
            )

        return queryset


class ExportUsersView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()

        data = []
        for user in queryset:
            data.append([
                user.id,
                user.get_full_name(),
                user.email,
                user.document,
                user.get_user_type_display(),
                'Ativo' if user.is_active else 'Inativo'
            ])

        df = pd.DataFrame(
            data,
            columns=['ID', 'NOME', 'EMAIL', 'CPF/CNPJ', 'TIPO', 'STATUS']
        )

        buffer = io.BytesIO()

        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Usuários')

        buffer.seek(0)

        response = HttpResponse(
            buffer.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
        response['Content-Disposition'] = 'attachement; filename="Relatório_Usuários.xlsx"'

        return response


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