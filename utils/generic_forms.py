from django import forms

class GenericForm(forms.ModelForm):
    is_active = forms.ChoiceField(
        choices=[('True', 'Ativo'), ('False', 'Inativo')],
        widget=forms.Select,
        label='Status da conta'
    )

    class Meta:
        model = None
        fields = '__all__'