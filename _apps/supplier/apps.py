from django.apps import AppConfig

app_name = 'supplier'

class SupplierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '_apps.supplier'
    verbose_name = 'Fornecedores'