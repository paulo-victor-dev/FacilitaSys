from django.db import models

from .product import Product
from .abstracts import *
from .attributes import AttributeValue

class Variant(TimeStampModel, ActiveModel, models.Model):
    # Variant identity
    sku = models.CharField(max_length=18, unique=True, verbose_name='SKU')

    bar_code = models.CharField(max_length=13, unique=True, verbose_name='Código de barras')
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variant_product', verbose_name='Produto')

    variation = models.ManyToManyField(
        AttributeValue,
        through='VariantOption', 
        related_name='variant_option', 
        verbose_name='Variação')

    # General infos
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Preço')

    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantidade')
        
    def __str__(self):
        variations = " ".join([str(var.value) for var in self.variation.all()])
        return f'{self.product} {variations}'

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'


class VariantOption(models.Model):
    variant = models.ForeignKey(
        Variant, 
        on_delete=models.CASCADE,
        verbose_name='Variante'
        )
    
    attribute = models.ForeignKey(
        AttributeValue, 
        on_delete=models.CASCADE,
        verbose_name='Opções'
        )

    def __str__(self):
        return ''

    class Meta:
        unique_together = ('variant', 'attribute')
        verbose_name = 'Opção da variante'
        verbose_name_plural = 'Opções da variante'
