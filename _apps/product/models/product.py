from django.db import models

from .attributes import Brand, Category, ProductModel
from .abstracts import *


class Product(TimeStampModel, ActiveModel, models.Model):
    PRODUCT_TYPE_CHOICES = (
        ('unidade', 'Un'),
        ('quilo', 'Kg'),
        ('peça', 'Pç'),
    )

    PRODUCT_FORMAT_CHOICES = (
        ('simples', 'Simples'),
        ('com_variacao', 'Com variação')
    )

    bar_code = models.BigIntegerField(unique=True, verbose_name='Código de barras')

    # Product identity
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product_category', verbose_name='Categoria')

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='product_brand', verbose_name='Marca')

    model = models.ForeignKey(ProductModel, on_delete=models.PROTECT, related_name='product_model', verbose_name='Modelo')

    unit_type = models.CharField(
        max_length=50,
        choices=PRODUCT_TYPE_CHOICES,
        default='unidade',
        verbose_name='Tipo de unidade'
    )

    format_type = models.CharField(
        max_length=50,
        choices=PRODUCT_FORMAT_CHOICES,
        default='simples',
        verbose_name='Formato'
    )

    # General infos
    description = models.TextField(max_length=255, blank=True, verbose_name='Descrição')
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Preço')
    stock = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name='Estoque')

    # Promo
    promo_price = models.DecimalField(default=0, max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Preço promocional')
    promo_start = models.DateField(null=True, blank=True, verbose_name='Início promoção')
    promo_end = models.DateField(null=True, blank=True, verbose_name='Fim promoção') 

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['category', 'brand', 'model']

    def __str__(self):
        return f"{self.category} {self.brand} {self.model}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='Imagens do produto')

    class Meta:
        verbose_name = 'Imagem do produto'
        verbose_name_plural = 'Imagens do produto'
