from django.urls import path

from .views import *

app_name = 'product'

urlpatterns = [
    # List
    path('product_list/', ProductListView.as_view(), name='product_list'),

    # Export
    path('product_list/export/', ExportProductsView.as_view(), name='product_list_export'),

    # CRUD Product
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # CRUD Brand
    path('brand_create/', BrandCreateView.as_view(), name='brand_create'),

    # CRUD Category
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),

    # CRUD Model
    path('model_create/', ProductModelCreateView.as_view(), name='model_create'),
]