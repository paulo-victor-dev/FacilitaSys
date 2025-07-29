from django import forms

from .models.product import Product
from.models.variant import Variant

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'bar_code', 'brand', 'category', 'model', 'unit_type', 'description', 'price', 'quantity')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        
        if price < 0:
            raise forms.ValidationError('O preço não pode ser negativo.')

        return price
        
class VariantCreationForm(forms.ModelForm):
    class Meta:
        model = Variant
        fields = ('bar_code', 'variation', 'price', 'quantity')