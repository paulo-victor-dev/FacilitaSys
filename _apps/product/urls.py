from django.urls import path

from .views import ProductListView, ExportProductsView

app_name = 'product'

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_list/export/', ExportProductsView.as_view(), name='product_list_export')
]