from django.db import models

from .attributes import Brand, Category, ProductModel
from .abstracts import *


class Product(TimeStampModel, ActiveModel, models.Model):
    PRODUCT_TYPE_CHOICES = (
        ('un', 'Un.'),
        ('kg', 'Kg.'),
        ('pç', 'Pç.'),
    )

    sku = models.CharField(max_length=18, unique=True, verbose_name='SKU')

    bar_code = models.CharField(max_length=13, unique=True, verbose_name='Código de barras')

    # Product identity
    name = models.CharField(max_length=50, unique=True, verbose_name='Nome')

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, blank=True, null=True, related_name='product_brand', verbose_name='Marca')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True, related_name='product_category', verbose_name='Categoria')

    model = models.ForeignKey(ProductModel, on_delete=models.PROTECT, blank=True, null=True, related_name='product_model', verbose_name='Modelo')

    unit_type = models.CharField(
        max_length=50,
        choices=PRODUCT_TYPE_CHOICES,
        default='un',
        verbose_name='Tipo de unidade'
    )

    # General infos
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name='Descrição')

    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Preço')

    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantidade')

    def __str__(self):
        return f"{self.name} {self.brand if self.brand else ''}"
    
    def save(self, *args, **kwargs):
        if not self.sku:
            name_tag = self.name[0:3].upper()

            brand_tag = f'-{self.brand.name[0:3].upper()}' if self.brand else ''

            self.sku = f'{name_tag}{brand_tag}'
        
        super().save(*args, **kwargs)
            

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-id']

