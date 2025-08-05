from django import template

register = template.Library()

@register.filter
def cpf_cnpj_mask(value):
    if len(value) == 11:
        return f'{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:]}'
    
    elif len(value) == 14:
        return f'{value[:2]}.{value[2:5]}.{value[5:8]}/{value[8:12]}-{value[12:]}'

@register.filter
def get_field(obj, field_name):
    val = getattr(obj, field_name)

    return val() if callable(val) else val