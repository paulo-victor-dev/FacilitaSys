from django import forms

from .models.product import Product

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'bar_code', 'brand', 'category', 'model', 'unit_type', 'description', 'price', 'quantity', 'promo_price', 'promo_start', 'promo_end')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Este campo é obrigatório.')
        
        if Product.objects.filter(name=name).exists():
            raise forms.ValidationError('Produto já cadastrado com esse nome.')

        return name