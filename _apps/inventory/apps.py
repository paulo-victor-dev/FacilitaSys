from django.apps import AppConfig

app_name = 'inventory'

class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '_apps.inventory'
    verbose_name = 'Inventário'
