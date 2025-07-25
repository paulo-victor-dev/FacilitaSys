from django.contrib import admin

from .models.product import Product, ProductImage
from .models.attributes import *
from .models.variant import Variant, VariantOption


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class VariantProductInline(admin.TabularInline):
    model = Variant
    extra = 1

class VariantOptionInline(admin.TabularInline):
    model = VariantOption
    extra = 1


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('_name', 'sku', 'bar_code', 'is_active', 'creation_date', 'update_date')
    search_fields = ('id', '_name', 'sku', 'bar_code')
    list_filter = ('is_active',)
    readonly_fields = ('id',)
    inlines = [VariantOptionInline]

    def _name(self, obj):
        return obj.__str__()
    _name.short_description = 'Descrição'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('_name', 'sku', 'bar_code', 'is_active', 'creation_date', 'update_date')
    search_fields = ('id', '_name', 'sku', 'bar_code')
    list_filter = ('is_active',)
    inlines = [VariantProductInline, ProductImageInline]

    def _name(self, obj):
        return obj.__str__()
    _name.short_description = 'Descrição'


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('id', 'name')


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('value',)
    search_fields = ('id', 'value')


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


