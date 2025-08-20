from utils.generic_views import *

from .models.product import Product
from .models.attributes import Brand, Category, ProductModel 

from .forms import ProductForm

# Product
class ProductListView(GenericListView):
    model = Product
    headers = ['#', 'NOME', 'SKU', 'PREÇO', 'QUANTIDADE', 'STATUS']
    fields = ['id', '__str__', 'sku', 'price', 'quantity', 'is_active']
    search_fields = ['id', '__str__', 'sku']

class ProductCreateView(GenericCreateView):
    model = Product
    form_class = ProductForm
    
class ProductUpdateView(GenericUpdateView):
    model = Product
    form_class = ProductForm

class ProductDeleteView(GenericDeleteView):
    model = Product
    forbid_self_delete = True
    
class ExportProductsView(GenericExportView):
    model = Product
    headers = ['#', 'NOME', 'SKU', 'PREÇO', 'QUANTIDADE', 'STATUS']
    fields = ['id', '__str__', 'sku', 'price', 'quantity', 'is_active']


# Brand
class BrandListView(GenericListView):
    model = Brand
    headers = ['#', 'NOME', 'STATUS']
    fields = ['id', 'name', 'is_active']
    search_fields = ['id', 'name']

class BrandCreateView(GenericCreateView):
    model = Brand
    
class BrandUpdateView(GenericUpdateView):
    model = Brand

class BrandDeleteView(GenericDeleteView):
    model = Brand
    forbid_self_delete = True

class ExportBrandsView(GenericExportView):
    model = Brand
    headers = ['#', 'NOME']
    fields = ['id', 'name']


# Category
class CategoryListView(GenericListView):
    model = Category
    headers = ['#', 'NOME', 'STATUS']
    fields = ['id', 'name', 'is_active']
    search_fields = ['id', 'name']

class CategoryCreateView(GenericCreateView):
    model = Category

class CategoryUpdateView(GenericUpdateView):
    model = Category

class CategoryDeleteView(GenericDeleteView):
    model = Category
    forbid_self_delete = True

class ExportCategorysView(GenericExportView):
    model = Category
    headers = ['#', 'NOME']
    fields = ['id', 'name']


# Model
class ProductModelListView(GenericListView):
    model = ProductModel
    headers = ['#', 'NOME', 'STATUS']
    fields = ['id', 'name', 'is_active']
    search_fields = ['id', 'name']

class ProductModelCreateView(GenericCreateView):
    model = ProductModel

class ProductModelUpdateView(GenericUpdateView):
    model = ProductModel

class ProductModelDeleteView(GenericDeleteView):
    model = ProductModel
    forbid_self_delete = True

class ExportProductModelsView(GenericExportView):
    model = ProductModel
    headers = ['#', 'NOME']
    fields = ['id', 'name']
