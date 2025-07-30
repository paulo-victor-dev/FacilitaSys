from django import forms

from .models.product import Product
from.models.attributes import Brand, Category, ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'bar_code', 'sku', 'brand', 'category', 'model', 'unit_type', 'description', 'price', 'quantity')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        
        if price < 0:
            raise forms.ValidationError('O preço não pode ser negativo.')

        return price

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ('name',)