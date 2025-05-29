from django.db import models


class TimeStampModel(models.Model):
    """Date Control"""
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    """State control"""
    is_active = models.BooleanField(default=True, verbose_name='Situação', help_text='Define se o item está ativo.')
    
    class Meta:
        abstract = True