from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from _apps.product.models.abstracts import *

class Supplier(TimeStampModel, ActiveModel, models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')

    email = models.EmailField(max_length=254, blank=True, null=True, verbose_name='Email')

    document = models.CharField(max_length=14, unique=True, blank=True, null=True, verbose_name='CNPJ')

    phone = PhoneNumberField(blank=True, null=True, verbose_name='Telefone')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['id']