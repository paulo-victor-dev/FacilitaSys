from django.urls import path

from .views import ProductListView, ExportProductsView

app_name = 'product'

urlpatterns = [
    # List
    path('product_list/', ProductListView.as_view(), name='product_list'),

   # Export
    path('product_list/export/', ExportProductsView.as_view(), name='product_list_export'),

    # CRUD
    # path('product_create/', .as_view(), name='product_create'),
    # path('product_update/<int:pk>/', .as_view(), name='product_update'),
    # path('product_delete/<int:pk>/', .as_view(), name='product_delete'),
]