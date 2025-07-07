from django.urls import path

from .views import ProductListView, ExportProductsView, ProductCreateView

app_name = 'product'

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='create'),

    path('product_list/export/', ExportProductsView.as_view(), name='product_list_export'),
]