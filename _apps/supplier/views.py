from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Supplier

class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'