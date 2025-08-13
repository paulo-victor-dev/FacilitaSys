from django.urls import path

from .views import *

app_name = 'product'

urlpatterns = [
    # List
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('brand_list/', BrandListView.as_view(), name='brand_list'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('model_list/', ProductModelListView.as_view(), name='model_list'),

    # Export
    path('export/', ExportProductsView.as_view(), name='product_export'),
    path('export/', ExportBrandsView.as_view(), name='brand_export'),
    path('export/', ExportCategorysView.as_view(), name='category_export'),
    path('export/', ExportProductModelsView.as_view(), name='productmodel_export'),

    # CRUD Product
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # CRUD Brand
    path('brand_create/', BrandCreateView.as_view(), name='brand_create'),
    path('brand_update/<int:pk>/', BrandUpdateView.as_view(), name='brand_update'),
    path('brand_delete/<int:pk>/', BrandDeleteView.as_view(), name='brand_delete'),

    # CRUD Category
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    # CRUD Model
    path('model_create/', ProductModelCreateView.as_view(), name='productmodel_create'),
    path('model_update/<int:pk>/', ProductModelUpdateView.as_view(), name='productmodel_update'),
    path('model_delete/<int:pk>/', ProductModelDeleteView.as_view(), name='productmodel_delete'),
]