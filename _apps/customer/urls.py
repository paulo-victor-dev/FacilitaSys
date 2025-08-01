from django.urls import path

from .views import *

app_name = 'customer'

urlpatterns = [
    # List
    path('customer_list/', CustomerListView.as_view(), name='customer_list'),

    # Export
    path('customer_list/export/', ExportCustomersView.as_view(), name='customer_list_export'),

    # CRUD
    path('customer_create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer_update/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer_delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
]