from django import forms

class GenericForm(forms.ModelForm):
    is_active = forms.ChoiceField(
        choices=[('True', 'Ativo'), ('False', 'Inativo')],
        widget=forms.Select,
        label='Status'
    )

    class Meta:
        model = None
        fields = '__all__'
        exclude = ('',)

    def __init__(self, fields=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if fields:
            allowed = set(fields)
            for field_name in list(self.fields):
                if field_name not in allowed:
                    self.fields.pop(field_name)

        fields_to_end = ['is_active', 'creation_date', 'update_date']
        for _field in fields_to_end:
            if _field in self.fields:
                self.fields[_field] = self.fields.pop(_field)
    