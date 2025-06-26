from django.urls import path

from .views import *

app_name = 'order'

urlpatterns = [
    # List
    path('order_list/', OrderListView.as_view(), name='order_list'),

    # Export
    path('order_list/export/', ExportOrdersView.as_view(), name='order_list_export'),

    # Detail
    path('detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
