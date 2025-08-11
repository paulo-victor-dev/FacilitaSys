from django.urls import path

from .views import *

app_name = 'order'

urlpatterns = [
    # List
    path('order_list/', OrderListView.as_view(), name='order_list'),

    # Export
    path('export/', ExportOrdersView.as_view(), name='order_export'),

    # CRUD
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('order_update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('order_delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
]
