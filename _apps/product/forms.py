from django import forms
from django.db.models import Count
from django.core.exceptions import ValidationError

from .models.product import Product
from .models.variant import Variant

class VariantForm(forms.ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'

    def clean(self):
        cleaned = super().clean()

        attrs = set(self.cleaned_data.get('variation', []).values_list('id', flat=True))
        if not attrs:
            return cleaned

        qs = Variant.objects.filter(product=self.instance.product)\
            .annotate(num=Count('variation'))\
            .filter(num=len(attrs), variation__in=attrs)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("Já existe variante com essas opções.")
        return cleaned