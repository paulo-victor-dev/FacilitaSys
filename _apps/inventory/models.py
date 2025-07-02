from django.db import models

from _apps.product.models.abstracts import TimeStampModel
from _apps.product.models.product import Product
from _apps.supplier.models import Supplier


class Flow(TimeStampModel, models.Model):
    FLOW_CHOICES = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )

    ORIGIN_CHOICES = (
        ('fornecedor', 'Fornecedor'),
        ('manual', 'Manual'),
    )

    DESTINATION_CHOICES = (
        ('cliente', 'Cliente final'),
        ('estoque', 'Estoque'),
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT, 
        blank=True, 
        null=True, 
        related_name='flow_supplier', 
        verbose_name='Fornecedor'
    )

    flow_type = models.CharField(
        max_length=50,
        choices=FLOW_CHOICES,
        default='entrada',
        verbose_name='Tipo de movimentação'
    )

    origin = models.CharField(
        max_length=50,
        choices=ORIGIN_CHOICES,
        default='fornecedor',
        verbose_name='Origem'
    )

    destination = models.CharField(
        max_length=50,
        choices=DESTINATION_CHOICES,
        default='cliente',
        verbose_name='Destino'
    )

    def __str__(self):
        return f'Movimentação ({self.id})'

    class Meta:
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'
        ordering = ['id']


class FlowItem(models.Model):
    flow = models.ForeignKey(
        Flow, 
        on_delete=models.PROTECT, 
        related_name='flowitem_flow', 
        verbose_name='Movimentação'
    )

    product = models.ForeignKey(
        Product, 
        on_delete=models.PROTECT, 
        related_name='flowitem_product', 
        verbose_name='Produto'
    )

    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantidade')

    def __str__(self):
        return 'Item da movimentação'

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'