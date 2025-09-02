from django.contrib.auth import forms as auth_forms
from django import forms

from .models import User
from utils.generic_forms import GenericForm


class LoginForm(auth_forms.AuthenticationForm):
    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
                
                if not user.check_password(password):
                    raise forms.ValidationError('Email ou senha incorretos.')
                
            except User.DoesNotExist:
                raise forms.ValidationError('Email ou senha incorretos.')

        return super().clean()


class UserCreateForm(auth_forms.UserCreationForm):    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'user_type', 'is_active')

    # def clean_first_name(self):
    #     first_name = self.cleaned_data.get('first_name')
    #     if not first_name:
    #         raise forms.ValidationError('Este campo é obrigatório.')
    #     return first_name
    
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('Este e-mail já está cadastrado.')
    #     return email
    

class UserUpdateForm(GenericForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'user_type', 'is_active')

        def clean_first_name(self):
            first_name = self.cleaned_data.get('first_name')
            if not first_name:
                raise forms.ValidationError('Este campo é obrigatório.')
            return first_name