from django.db import models

from .product import Product
from .attributes import Attribute, AttributeValue
from .abstracts import *


class Variant(TimeStampModel, ActiveModel, models.Model):
    sku = models.CharField(max_length=30, unique=True, verbose_name='SKU')

    # Varaint identity
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variant_product', verbose_name='Produto')

    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, verbose_name='Atributo')

    option = models.ForeignKey(AttributeValue, on_delete=models.CASCADE, verbose_name='Opção')

    # General infos
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Preço')

    stock = models.PositiveIntegerField(default=0, verbose_name='Estoque')

    # Variant image 
    image = models.ImageField(upload_to='variant_images/', null=True, blank=True, verbose_name='Imagem')

    class Meta:
        unique_together = ('product', 'option')
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
    
    def __str__(self):
        return f'{self.product} {self.option}'