from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError

from .models.variant import Variant

@receiver(m2m_changed, sender=Variant.option.through)
def generete_variant_sku(sender, instance, action, **kwargs):
    if action == 'post_add':
        if not instance.sku:
            sku = instance.generate_sku()

            if Variant.objects.filter(sku=sku).exists():
                raise ValidationError('Esse SKU já existe!')

            instance.sku = sku
            instance.save(update_fields=['sku'])