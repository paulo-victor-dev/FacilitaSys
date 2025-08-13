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
    template_name = 'add_pages/product_add.html'
    success_url = reverse_lazy('product:product_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Produto cadastrado com sucesso!')
        return super().form_valid(form)

class ProductUpdateView(GenericUpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_pages/product_update.html'
    success_url = reverse_lazy('product:product_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Produto atualizado com sucesso!')
        return super().form_valid(form)

class ProductDeleteView(GenericDeleteView):
    model = Product
    template_name = 'delete_pages/product_delete.html'
    success_url = reverse_lazy('product:product_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Produto deletado com sucesso!')
        return super().form_valid(form)

class ExportProductsView(GenericExportView):
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()

        data = []
        for product in queryset:
            data.append([
                product.id,
                product.name,
                product.bar_code,
                product.quantity,
                product.price,
                'Ativo' if product.is_active else 'Inativo'
            ])

        df = pd.DataFrame(
            data,
            columns=['ID', 'NOME', 'CÓD. BARRAS', 'QUANTIDADE', 'PREÇO', 'STATUS']
        )

        buffer = io.BytesIO()

        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Produtos')

        buffer.seek(0)

        response = HttpResponse(
            buffer.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
        response['Content-Disposition'] = 'attachement; filename="Relatório_Produtos.xlsx"'

        return response


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
