from django import forms
from django.contrib.auth import forms as auth_forms

#import re

#from validate_docbr import CPF, CNPJ

from .models import User


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


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'user_type', 'is_active')

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError('Este campo é obrigatório.')
        return first_name
    
    # def clean_document(self):
    #     document = self.cleaned_data.get('document')

    #     if not document:
    #         raise forms.ValidationError('Este campo é obrigatório.')
        
    #     doc_only_digits = re.sub(r'\D', '', document)

    #     if CPF().validate(doc_only_digits) or CNPJ().validate(doc_only_digits):
    #         return doc_only_digits
    #     else:
    #         raise forms.ValidationError('CPF/CNPJ inválido.')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado.')
        return email

  
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'user_type', 'is_active')

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError('Este campo é obrigatório.')
        return first_name
    
    # def clean_document(self):
    #     document = self.cleaned_data.get('document')

    #     if not document:
    #         raise forms.ValidationError('Este campo é obrigatório.')
        
    #     doc_only_digits = re.sub(r'\D', '', document)

    #     if CPF().validate(doc_only_digits) or CNPJ().validate(doc_only_digits):
    #         return doc_only_digits
    #     else:
    #         raise forms.ValidationError('CPF/CNPJ inválido.')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este e-mail já está sendo usado por outro usuário.")

        return email