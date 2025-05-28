from django.contrib import admin

from .models import Product, Category, ProductModel, Type, Color, Size, ProductVariant, VariantImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'model', 'type', 'is_active', 'creation_date', 'update_date')
    search_fields = ('category__name', 'model__name', 'type__name', 'is_active')


class VariantImageInLine(admin.TabularInline):
    model = VariantImage
    extra = 1

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'color', 'size', 'stock', 'is_active', 'creation_date', 'update_date')
    search_fields = ('product__category__name', 'product__model__name', 'product__type__name', 'color__name', 'size__name')
    inlines = [VariantImageInLine]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name', 'id')


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name', 'id')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name', 'id')


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name', 'id')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name', 'id')

