from django import forms

import re
from validate_docbr import CPF

from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'cpf')

        def clean_cpf(self):
            cpf = self.cleaned_data.get('cpf')
            
            cpf_only_digits = re.sub(r'\D', '', cpf)

            if CPF().validate(cpf_only_digits):
                return cpf_only_digits
            else:
                raise forms.ValidationError('CPF inválido.')