from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Por favor, forneça um e-mail válido!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'funcionario')
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'admin')
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('admin', 'Administrador'),
        ('funcionario', 'Funcionário'),
    )

    first_name = models.CharField(max_length=50, blank=True, verbose_name='Nome')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Sobrenome')
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(
        default=False, 
        verbose_name='Conta ativa?',
        help_text='Se marcado, o usuário poderá acessar ao site normalmente.'
    )

    is_staff = models.BooleanField(
        default=False, 
        verbose_name='Acesso ao painel administrativo?',
        help_text='Se marcado, esse usuário terá acesso a esse painel administrativo.'
    )
    
    is_superuser = models.BooleanField(
        default=False, 
        verbose_name='Permissões de administrador?', 
        help_text='Se marcado, esse usuário terá acesso total ao sistema.'
    )

    user_type = models.CharField(
        max_length=50,
        choices=USER_TYPE_CHOICES,
        default='funcionario',
        verbose_name='Tipo de usuário'
    )

    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Data de cadastro')

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'