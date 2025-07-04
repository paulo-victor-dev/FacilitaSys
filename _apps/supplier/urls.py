from django.urls import path

from .views import *

app_name = 'supplier'

urlpatterns = [
    path('supplier_list/', SupplierListView.as_view(), name='supplier_list')
]
