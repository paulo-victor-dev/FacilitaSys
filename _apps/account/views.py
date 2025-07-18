from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.contrib.auth import views as auth_views
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from django.db.models import Q

from django.http import HttpResponse

import io, pandas as pd

from .forms import LoginForm, UserCreationForm, UserUpdateForm
from .models import User


class LoginView(auth_views.LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('account:login')


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'list_pages/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        qs = User.objects.all()

        search = self.request.GET.get('search')

        if search:
            qs = qs.filter(
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(email__icontains=search)
            )
        return qs


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'add_pages/user_add.html'
    success_url = reverse_lazy('account:user_list')

    def form_valid(self, form):
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'update_pages/user_update.html'
    success_url = reverse_lazy('account:user_list')

    def form_valid(self, form):
        messages.success(self.request, 'Usuário atualizado com sucesso!')
        return super().form_valid(form)
    

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'delete_pages/user_confirm_delete.html'
    success_url = reverse_lazy('account:user_list')

    def form_valid(self, form):
        if self.get_object() == self.request.user:
            messages.error(self.request, 'Não é possível excluir sua própria conta enquanto estiver logado.')
            return self.form_invalid(form)

        messages.success(self.request, 'Usuário excluído com sucesso!')
        return super().form_valid(form)
        

class ExportUsersView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()

        data = []
        for user in queryset:
            data.append([
                user.id,
                user.get_full_name(),
                user.email,
                user.get_user_type_display(),
                'Ativo' if user.is_active else 'Inativo'
            ])

        df = pd.DataFrame(
            data,
            columns=['ID', 'NOME', 'EMAIL', 'TIPO', 'STATUS']
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
