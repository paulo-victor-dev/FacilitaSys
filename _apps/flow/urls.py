from django.urls import path

from .views import *

app_name = 'flow'

urlpatterns = [
    # List
    path('flow_list/', FlowListView.as_view(), name='flow_list'),

    # Export
    path('export/', ExportFlowsView.as_view(), name='flow_export'),

    # CRUD
    path('flow_create/', FlowCreateView.as_view(), name='flow_create'),
    path('flow_update/<int:pk>/', FlowUpdateView.as_view(), name='flow_update'),
    path('flow_delete/<int:pk>/', FlowDeleteView.as_view(), name='flow_delete'),
]
