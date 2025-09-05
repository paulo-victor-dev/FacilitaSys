from utils.generic_views import *

from .models import Supplier
from .forms import SupplierForm

class SupplierListView(GenericListView):
    model = Supplier
    headers = ['#', 'NOME', 'CNPJ', 'EMAIL', 'STATUS']
    fields = ['id', 'name', 'cnpj', 'email', 'is_active']
    search_fields = ['id', 'name', 'cnpj', 'email']


class SupplierCreateView(GenericCreateView):
    model = Supplier


class SupplierUpdateView(GenericUpdateView):
    model = Supplier


class SupplierDeleteView(GenericDeleteView):
    model = Supplier
    forbid_self_delete = True


class ExportSuppliersView(GenericExportView):
    model = Supplier
    headers = ['#', 'NOME', 'CNPJ', 'EMAIL', 'STATUS']
    fields = ['id', 'name', 'cnpj', 'email', 'is_active']

