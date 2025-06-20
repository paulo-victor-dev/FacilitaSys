from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

from .models import Order


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        total_itens =  Order.objects.annotate(total_itens=Sum('orderItem_order__quantity'))

        return total_itens
    

    