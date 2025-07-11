from django.urls import path

from .views import *

app_name = 'supplier'

urlpatterns = [
    # List
    path('supplier_list/', SupplierListView.as_view(), name='supplier_list'),

    # Export
    # path('supplier_list/export/', ..., name='supplier_list_export'),

    # # CRUD
    # path('supplier_create/', ..., name='supplier_create'),
    # path('supplier_update/<int:pk>/', ..., name='supplier_update'),
    # path('supplier_delete/<int:pk>/', ..., name='supplier_delete'),
]
