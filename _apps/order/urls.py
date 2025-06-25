from django.urls import path

from .views import OrderListView, ExportOrdersView

app_name = 'order'

urlpatterns = [
    path('order_list/', OrderListView.as_view(), name='order_list'),
    path('order_list/export/', ExportOrdersView.as_view(), name='order_list_export'),
]
