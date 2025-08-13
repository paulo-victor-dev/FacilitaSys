from django import forms

from .models.product import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'bar_code', 'sku', 'brand', 'category', 'model', 'unit_type', 'description', 'price', 'quantity', 'is_active')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        
        if price < 0:
            raise forms.ValidationError('O preço não pode ser negativo.')

        return price