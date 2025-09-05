from django import forms

from collections import OrderedDict
import re
from validate_docbr import CNPJ


class GenericForm(forms.ModelForm):
    is_active = forms.ChoiceField(
        choices=[('True', 'Ativo'), ('False', 'Inativo')],
        widget=forms.Select,
        label='Status'
    )

    class Meta:
        model = None
        fields = '__all__'

       

    def __init__(self, fields=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if fields:
            allowed = set(fields)
            for field_name in list(self.fields):
                if field_name not in allowed:
                    self.fields.pop(field_name)

            self.fields = OrderedDict((f, self.fields[f]) for f in fields if f in self.fields)

        fields_to_end = ['is_active', 'creation_date', 'update_date']
        for _field in fields_to_end:
            if _field in self.fields:
                self.fields[_field] = self.fields.pop(_field)
    
    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        
        cnpj_only_digits = re.sub(r'\D', '', cnpj)

        if CNPJ().validate(cnpj_only_digits):
            return cnpj_only_digits
        else:
            raise forms.ValidationError('CNPJ inválido.')