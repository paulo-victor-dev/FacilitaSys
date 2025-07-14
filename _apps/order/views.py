from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.db.models import Sum, Q, Value, F
from django.db.models.functions import Concat
from django.http import HttpResponse

import pandas as pd
import io

from .models import Order


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'list_pages/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset =  Order.objects.annotate(
            total_itens=Sum('orderItem_order__quantity'),

            full_name=Concat(
                F('customer__first_name'),
                Value(' '),
                F('customer__last_name'),
            ),
        )

        search = self.request.GET.get('search')
        search_filter = self.request.GET.get('filter')

        if search and search_filter:
            lookup = f'{search_filter}__icontains'

            queryset = queryset.filter(
                Q(**{lookup: search})
            )

        return queryset


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'detail_includes/order_detail.html'
    context_object_name = 'order'    


class ExportOrdersView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        queryset = Order.objects.all()

        data = []
        for order in queryset:
            data.append([
                order.id,
                order.customer.get_full_name(),
                order.customer.document,
                order.orderItem_order.aggregate(Sum('quantity'))['quantity__sum'],
                order.total,
                order.creation_date.strftime('%d/%m/%Y'),
                order.get_status_display()
            ])


        df = pd.DataFrame(
            data,
            columns=['ID', 'CLIENTE', 'DOCUMENTO', 'QTD. ITENS', 'TOTAL', 'DATA', 'STATUS']
        )

        buffer = io.BytesIO()

        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Pedidos')

        buffer.seek(0)

        response = HttpResponse(
            buffer.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
        response['Content-Disposition'] = 'attachement; filename="Relatório_Pedidos.xlsx"'

        return response

    