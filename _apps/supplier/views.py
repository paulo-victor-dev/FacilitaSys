from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from django.db.models import Q, Value, F
from django.db.models.functions import Concat

from django.http import HttpResponse

import io, pandas as pd

from .models import Supplier
from .forms import SupplierForm

class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    paginate_by = 11
    template_name = 'list_pages/supplier_list.html'
    context_object_name = 'suppliers'

    def get_queryset(self):
        qs = super().get_queryset()

        search = self.request.GET.get('search', '')

        if search:
            qs = qs.filter(
                Q(id__icontains=search) |
                Q(name__icontains=search) |
                Q(cnpj__icontains=search) |
                Q(email__icontains=search)
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
    

class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'add_pages/supplier_add.html'
    success_url = reverse_lazy('supplier:supplier_list')

    def form_valid(self, form):
        messages.success(self.request, 'Fornecedor cadastrado com sucesso!')
        return super().form_valid(form)


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'update_pages/supplier_update.html'
    success_url = reverse_lazy('supplier:supplier_list')

    def form_valid(self, form):
        messages.success(self.request, 'Fornecedor atualizado com sucesso!')
        return super().form_valid(form)


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'delete_pages/supplier_delete.html'
    success_url = reverse_lazy('supplier:supplier_list')

    def form_valid(self, form):
        messages.success(self.request, 'Fornecedor excluído com sucesso!')
        return super().form_valid(form)
    

class ExportSuppliersView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        queryset = Supplier.objects.all()

        data = []
        for supplier in queryset:
            data.append([
                supplier.id,
                supplier,
                supplier.cnpj,
                supplier.email,
                'Ativo' if supplier.is_active else 'Inativo'
            ])

        df = pd.DataFrame(
            data,
            columns=['ID', 'NOME', 'CNPJ', 'EMAIL', 'STATUS']
        )

        buffer = io.BytesIO()

        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Fornecedores')

        buffer.seek(0)

        response = HttpResponse(
            buffer.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
        response['Content-Disposition'] = 'attachement; filename="Relatório_Fornecedores.xlsx"'

        return response