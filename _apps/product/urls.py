from django.urls import path

from .views import *

app_name = 'product'

urlpatterns = [
    # List
    path('product_list/', ProductListView.as_view(), name='product_list'),

    # Export
    path('product_list/export/', ExportProductsView.as_view(), name='product_list_export'),

    # CRUD
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]