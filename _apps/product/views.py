from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from django.db.models import Q

from django.http import HttpResponse

import pandas as pd
import io

from .models.product import Product
from .models.attributes import Brand, Category, ProductModel 

from .forms import *

# Product
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 11
    template_name = 'list_pages/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = super().get_queryset()

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

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_pages/product_add.html'
    success_url = reverse_lazy('product:product_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Produto cadastrado com sucesso!')
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_pages/product_update.html'
    success_url = reverse_lazy('product:product_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Produto atualizado com sucesso!')
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'delete_pages/product_delete.html'
    success_url = reverse_lazy('product:product_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Produto deletado com sucesso!')
        return super().form_valid(form)

class ExportProductsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()

        data = []
        for product in queryset:
            data.append([
                product.id,
                product.name,
                product.bar_code,
                product.quantity,
                product.price,
                'Ativo' if product.is_active else 'Inativo'
            ])

        df = pd.DataFrame(
            data,
            columns=['ID', 'NOME', 'CÓD. BARRAS', 'QUANTIDADE', 'PREÇO', 'STATUS']
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


# Brand
class BrandCreateView(LoginRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'add_pages/brand_add.html'
    success_url = reverse_lazy('product:product_create')

    def form_valid(self, form):
        messages.success(self.request, 'Marca cadastrada com sucesso!')
        return super().form_valid(form)


# Category
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_pages/category_add.html'
    success_url = reverse_lazy('product:product_create')

    def form_valid(self, form):
        messages.success(self.request, 'Categoria cadastrada com sucesso!')
        return super().form_valid(form)

# Model
class ProductModelCreateView(LoginRequiredMixin, CreateView):
    model = ProductModel
    form_class = ProductModelForm
    template_name = 'add_pages/model_add.html'
    success_url = reverse_lazy('product:product_create')

    def form_valid(self, form):
        messages.success(self.request, 'Modelo cadastrado com sucesso!')
        return super().form_valid(form)