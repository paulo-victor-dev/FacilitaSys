from django.contrib.auth import views as auth_views

from _core.utils.generic_views import *

from .forms import LoginForm, UserForm
from .models import User


class LoginView(auth_views.LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('account:login')
    

class UserListView(GenericListView):
    model = User
    headers = ['#', 'NOME', 'EMAIL', 'TIPO DE USUÁRIO', 'STATUS']
    fields = ['id', 'get_full_name', 'email', 'get_user_type_display', 'is_active']
    search_fields = ['id', 'first_name', 'last_name', 'email']
    obj_page_title = 'Usuários'
    obj_content_title = 'Usuários'


class UserCreateView(GenericCreateView):
    model = User
    form_class = UserForm


class UserUpdateView(GenericUpdateView):
    model = User
    form_class = UserForm


class UserDeleteView(GenericDeleteView):
    model = User
    forbid_self_delete = True 
        

class ExportUsersView(GenericExportView):
    model = User
    headers = ['#', 'NOME', 'EMAIL', 'TIPO', 'STATUS']
    fields = ['id', 'get_full_name', 'email', 'get_user_type_display', 'is_active']
