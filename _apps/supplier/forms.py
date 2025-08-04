from django import forms

import re
from validate_docbr import CNPJ

from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'cnpj', 'email', 'is_active')

        def clean_cnpj(self):
            cnpj = self.cleaned_data.get('cnpj')
            
            cnpj_only_digits = re.sub(r'\D', '', cnpj)

            if CNPJ().validate(cnpj_only_digits):
                return cnpj_only_digits
            else:
                raise forms.ValidationError('CNPJ inválido.')