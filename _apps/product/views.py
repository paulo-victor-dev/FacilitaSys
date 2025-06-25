from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Value, F, CharField
from django.db.models.functions import Concat
from django.http import HttpResponse

import pandas as pd
import io

from .models.product import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.annotate(
            full_name=Concat(
                F('category__name'),
                Value(' '),
                F('brand__name'),
                Value(' '),
                F('model__name'),
                output_field=CharField()
            )
        )

        search = self.request.GET.get('search')
        search_filter = self.request.GET.get('filter')

        if search and search_filter:
            lookup = f'{search_filter}__icontains'

            queryset = queryset.filter(
                Q(**{lookup: search})
            )

        return queryset


class ExportProductsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()

        data = []
        for product in queryset:
            data.append([
                product.id,
                product,
                product.bar_code,
                product.get_format_type_display(),
                product.price,
                product.stock,
                'Ativo' if product.is_active else 'Inativo'
            ])

        df = pd.DataFrame(
            data,
            columns=['ID', 'DESCRIÇÃO', 'CÓD. BARRAS', 'TIPO', 'PREÇO', 'ESTOQUE', 'STATUS']
        )

        buffer = io.BytesIO()

        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Produtos')

        buffer.seek(0)

        response = HttpResponse(
            buffer.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
        response['Content-Disposition'] = 'attachement; filename="Relatório_Produtos.xlsx"'

        return response
            
  
        
        
