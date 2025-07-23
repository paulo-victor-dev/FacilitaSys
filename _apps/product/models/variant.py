from django.db import models

from .product import Product
from .attributes import AttributeValue
from .abstracts import *


class Variant(TimeStampModel, ActiveModel, models.Model):
    # Varaint identity
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variant_product', verbose_name='Produto')

    option = models.ManyToManyField(AttributeValue, related_name='variant_option', verbose_name='Opções')

    # General infos
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Preço')

    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantidade')

    # Variant image 
    image = models.ImageField(upload_to='variant_images/', null=True, blank=True, verbose_name='Imagem')
        
    def __str__(self):
        options = " ".join([str(opt.value) for opt in self.option.all()])
        return f'{self.product} {options}'
    
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'