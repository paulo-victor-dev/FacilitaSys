from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from django.db.models import Q, Value, F
from django.db.models.functions import Concat

from django.http import HttpResponse

import io, pandas as pd

from .models import Supplier

class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'list_pages/supplier_list.html'
    context_object_name = 'suppliers'