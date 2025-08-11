from utils.generic_views import *

from .models import Customer
from .forms import CustomerForm

class CustomerListView(GenericListView):
    model = Customer
    headers = ['#', 'NOME', 'CPF', 'EMAIL', 'STATUS']
    fields = ['id', 'name', 'cpf', 'email', 'is_active']
    search_fields = ['id', 'name', 'cpf', 'email']


class CustomerCreateView(GenericCreateView):
    model = Customer
    form_class = CustomerForm


class CustomerUpdateView(GenericUpdateView):
    model = Customer
    

class CustomerDeleteView(GenericDeleteView):
    model = Customer
    forbid_self_delete = True 
    

class ExportCustomersView(GenericExportView):
    model = Customer
    headers = ['#', 'NOME', 'CPF', 'EMAIL', 'STATUS']
    fields = ['id', 'name', 'cpf', 'email', 'is_active']