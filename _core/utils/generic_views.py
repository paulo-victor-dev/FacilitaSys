from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.db.models import Q

from django.http import HttpResponse

import io, pandas as pd


class GenericListView(LoginRequiredMixin, ListView):
    paginate_by = 11
    template_name = 'common/_list.html'
    context_object_name = 'objs'
    obj_page_title = ''
    obj_content_title = ''

    headers = []
    fields = []
    search_fields = []

    def get_queryset(self):
        qs = super().get_queryset()

        search = self.request.GET.get('search', '')

        if search and self.search_fields:
            queries = [Q(**{f"{f}__icontains": search}) for f in self.search_fields]

            combined = queries.pop()

            for q in queries:
                combined |= q
            
            qs = qs.filter(combined)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['headers'] = self.headers
        ctx['fields'] = self.fields
        ctx['urls'] = self.get_crud_urls()

        ctx['obj_page_title'] = self.obj_page_title
        ctx['obj_content_title'] = self.obj_content_title

        paginator = ctx.get('paginator')
        page_obj = ctx.get('page_obj')

        if paginator and page_obj:
            ctx['page_range'] = paginator.get_elided_page_range(
                number=page_obj.number,
                on_each_side=1,
                on_ends=1
            )

        return ctx
    
    def get_crud_urls(self):
        app = self.model._meta.app_label
        obj = self.model._meta.model_name

        urls = {
            'url_create': f'{app}:{obj}_create',
            'url_update': f'{app}:{obj}_update',
            'url_delete': f'{app}:{obj}_delete',
            'url_export': f'{app}:{obj}_export',
        }
        return urls
    

class GenericCreateView(LoginRequiredMixin, CreateView):
    template_name = 'common/_create.html'
    success_message = 'Registro criado com sucesso'

    def get_success_url(self):
        app = self.model._meta.app_label
        obj = self.model._meta.model_name
        
        return reverse_lazy(f'{app}:{obj}_list') 

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class GenericUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'common/_update.html'
    success_message = 'Registro atualizado com sucesso'

    def get_success_url(self):
        app = self.model._meta.app_label
        obj = self.model._meta.model_name
        
        return reverse_lazy(f'{app}:{obj}_list') 

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    

class GenericDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'common/_delete.html'
    success_message = 'Registro excluído com sucesso'
    forbid_self_delete = False

    def get_success_url(self):
        app = self.model._meta.app_label
        obj = self.model._meta.model_name
        
        return reverse_lazy(f'{app}:{obj}_list') 

    def form_valid(self, form):
        obj = self.get_object()

        if self.forbid_self_delete and obj == self.request.user:
            messages.error(
                self.request, 
                'Não é possível excluir sua própria conta enquanto estiver logado'
            )
            return self.form_invalid(form)

        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class GenericExportView(LoginRequiredMixin, View):
    model = None
    headers = []
    fields = []

    def get_queryset(self):
        return self.model.objects.all()

    def get_filename(self):
        return f'Relatório_{self.model._meta.model_name}'

    def get_row(self, obj):
        row = []

        for field in self.fields:
            value = getattr(obj, field)
            if callable(value):
                value = value()
            if isinstance(value, bool):
                value = 'ativo' if value else 'Inativo'
            row.append(value)
        
        return row

    def get(self, request, *args, **kwargs):
        data = [self.get_row(obj) for obj in self.get_queryset()]

        df = pd.DataFrame(data, columns=self.headers)

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Dados')

        buffer.seek(0)
        response = HttpResponse(
            buffer.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
        response['Content-Disposition'] = f'attachement; filename="{self.get_filename()}.xlsx"'
        return response

