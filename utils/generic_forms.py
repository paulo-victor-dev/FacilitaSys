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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        fields_to_end = ['is_active', 'creation_date', 'update_date']
        for _field in fields_to_end:
            if _field in self.fields:
                self.fields[_field] = self.fields.pop(_field)
    