from utils.generic_views import *

from .models import Flow

class FlowListView(GenericListView):
    model = Flow
    headers = ['#', 'FORNECEDOR', 'TIPO', 'ORIGEM', 'DESTINO', 'DATA']
    fields = ['id', 'supplier', 'get_flow_type_display', 'get_origin_display', 'get_destination_display', 'creation_date']
    search_fields = ['id', 'supplier', 'get_flow_type_display']

class FlowCreateView(GenericCreateView):
    model = Flow

class FlowUpdateView(GenericUpdateView):
    model = Flow

class FlowDeleteView(GenericDeleteView):
    model = Flow
    forbid_self_delete = True

class ExportFlowsView(GenericExportView):
    model = Flow
    headers = ['#', 'FORNECEDOR', 'TIPO', 'ORIGEM', 'DESTINO', 'DATA']
    fields = ['id', 'supplier', 'get_flow_type_display', 'get_origin_display', 'get_destination_display', 'creation_date']
   

    

