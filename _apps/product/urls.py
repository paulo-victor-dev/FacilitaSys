from django.urls import path

from .views import ProductListView

app_name = 'product'

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list')
]