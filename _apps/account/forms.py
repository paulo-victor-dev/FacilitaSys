from django import forms
from django.contrib.auth import forms as auth_forms

from .models import User


class LoginForm(auth_forms.AuthenticationForm):
    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
                
                if not user.check_password(password):
                    raise forms.ValidationError('Por favor, entre com um email e senha corretos.')
                
                if not user.is_active:
                    raise forms.ValidationError('Esta conta ainda não foi ativada. Verifique seu e-mail.')
                
            except User.DoesNotExist:
                raise forms.ValidationError('Por favor, entre com um email e senha corretos.')

        return super().clean()


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'cnpj', 'phone', 'password1', 'password2')

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError('Este campo é obrigatório.')
        return first_name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado.')
        return email
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not cpf:
            raise forms.ValidationError('Este campo é obrigatório.')
        return cpf
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError('Este campo é obrigatório.')
        return phone
    

class PasswordResetForm(auth_forms.PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Nenhuma conta foi encontrada com este e-mail.')
        return email