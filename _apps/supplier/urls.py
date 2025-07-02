from django.urls import path

from .views import *

urlpatterns = [
    path('supplier_list/', SupplierListView.as_view(), name='supplier_list')
]
