from utils.generic_views import *

from .models import Order


class OrderListView(GenericListView):
    model = Order
    headers = ['#', 'CLIENTE', 'TOTAL', 'DATA CRIAÇÃO','STATUS']
    fields = ['id', 'customer', 'total', 'creation_date', 'get_status_display']
    search_fields = ['id', 'customer', 'creation_date', 'status']


class OrderCreateView(GenericCreateView):
    model = Order
    #form_class = ''
    #template_name = ''


class OrderUpdateView(GenericUpdateView):
    model = Order


class OrderDeleteView(GenericDeleteView):
    model = Order


class ExportOrdersView(GenericExportView):
    model = Order
    headers = ['#', 'CLIENTE', 'TOTAL', 'DATA CRIAÇÃO','STATUS']
    fields = ['id', 'customer', 'total', 'creation_date', 'status']

    