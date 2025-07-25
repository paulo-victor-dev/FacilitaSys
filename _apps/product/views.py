from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q, Count

from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

import pandas as pd
import io

from .models.product import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 11
    template_name = 'list_pages/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = super().get_queryset()

        qs = qs.annotate(num_variants=Count('variant_product', distinct=True))

        search = self.request.GET.get('search', '')

        if search:
            qs = qs.filter(
                Q(id__icontains=search) |
                Q(name__icontains=search) |
                Q(sku__icontains=search) 
            )

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = context.get('paginator')
        page_obj = context.get('page_obj')

        if paginator and page_obj:
            context['page_range'] = paginator.get_elided_page_range(
                number=page_obj.number,
                on_each_side=1,
                on_ends=1
            )

        return context


class ExportProductsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()

        data = []
        for product in queryset:
            data.append([
                product.id,
                product.name,
                product.bar_code,
                product.get_format_type_display(),
                product.price,
                product.quantity,
                'Ativo' if product.is_active else 'Inativo'
            ])

        df = pd.DataFrame(
            data,
            columns=['ID', 'NOME', 'CÓD. BARRAS', 'TIPO', 'QUANTIDADE', 'PREÇO', 'STATUS']
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

        
        
