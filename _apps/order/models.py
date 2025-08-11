from django.db import models
from django.core.exceptions import ValidationError

from _apps.customer.models import Customer
from _apps.product.models.abstracts import *
from _apps.product.models.product import Product


class Order(TimeStampModel, models.Model):
    ORDER_STATUS = (
        ('finished', 'Finalizado'),
        ('pendent', 'Pendente'),
        ('canceled', 'Cancelado'),
    )

    customer = models.ForeignKey(
        Customer, 
        on_delete=models.PROTECT,
        related_name='order_customer',
        verbose_name='Cliente'
    )

    status = models.CharField(
        max_length=50, 
        choices=ORDER_STATUS,
        default='pendent',
        verbose_name='Status'
    )

    total = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Total')

    def __str__(self):
        return f'Pedido {self.id}'

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-id']
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderItem_order')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orderItem_product')

    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantidade')

    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço do item')

    @property
    def total(self):
        return self.unit_price * self.quantity
    
    def clean(self):
        super().clean()
        if self.quantity < 1:
            raise ValidationError({'quantity': 'Quantidade deve ser maior que 0.'})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.unit_price = self.product.price
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'
    
    
