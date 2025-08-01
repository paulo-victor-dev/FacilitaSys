from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from django.db.models import Q

from django.http import HttpResponse

import io, pandas as pd

from .models import Customer
from .forms import CustomerForm

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    paginate_by = 11
    template_name = 'list_pages/customer_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        qs = super().get_queryset()

        search = self.request.GET.get('search', '')

        if search:
            qs = qs.filter(
                Q(id__icontains=search) |
                Q(name__icontains=search) |
                Q(cpf__icontains=search) |
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


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'add_pages/customer_add.html'
    success_url = reverse_lazy('customer:customer_list')


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'update_pages/customer_update.html'
    success_url = reverse_lazy('customer:customer_list')

    def form_valid(self, form):
        messages.success(self.request, 'Cliente atualizado com sucesso!')
        return super().form_valid(form)
    

class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'delete_pages/customer_delete.html'
    success_url = reverse_lazy('customer:customer_list')

    def form_valid(self, form):
        messages.success(self.request, 'Cliente excluído com sucesso!')
        return super().form_valid(form)
    

class ExportCustomersView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        queryset = Customer.objects.all()

        data = []
        for customer in queryset:
            data.append([
                customer.id,
                customer,
                customer.cpf,
                customer.email,
                'Ativo' if customer.is_active else 'Inativo'
            ])

        df = pd.DataFrame(
            data,
            columns=['ID', 'NOME', 'CPF', 'EMAIL', 'STATUS']
        )

        buffer = io.BytesIO()

        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Clientes')

        buffer.seek(0)

        response = HttpResponse(
            buffer.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
        response['Content-Disposition'] = 'attachement; filename="Relatório_Clientes.xlsx"'

        return response