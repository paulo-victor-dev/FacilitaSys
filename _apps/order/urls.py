from django.urls import path

from .views import OrderListView

app_name = 'order'

urlpatterns = [
    path('order_list/', OrderListView.as_view(), name='order_list'),
]
