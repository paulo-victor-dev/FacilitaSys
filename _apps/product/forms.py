from django import forms

from .models.product import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['bar_code', 'category', 'brand', 'model', 'unit_type', 'format_type', 'price', 'stock']