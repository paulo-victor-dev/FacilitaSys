from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '_apps.product'
    verbose_name = 'Produtos'

    def ready(self):
        import _apps.product.signals
