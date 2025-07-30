from django.contrib import admin

from .models.product import Product
from .models.attributes import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('_name', 'sku', 'bar_code', 'is_active', 'creation_date', 'update_date')
    search_fields = ('id', '_name', 'sku', 'bar_code')
    list_filter = ('is_active',)

    def _name(self, obj):
        return obj.__str__()
    _name.short_description = 'Descrição'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('id', 'name')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('id', 'name')

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('id', 'name')


