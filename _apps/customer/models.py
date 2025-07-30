from django.db import models

from ..product.models.abstracts import *

class Customer(TimeStampModel, ActiveModel, models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name='Nome'
    )

    cpf = models.CharField(
        max_length=11, 
        unique=True, 
        blank=True, 
        null=True, 
        verbose_name='CPF'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'