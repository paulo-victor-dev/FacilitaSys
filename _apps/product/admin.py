from django.contrib import admin

from .models.product import Product, ProductImage
from .models.attributes import *
from .models.variant import Variant


class ProductImageInline(admin.TabularInline):
    model = ProductImage

class VariantProductInline(admin.TabularInline):
    model = Variant

class AttributeValueInline(admin.TabularInline):
    model = AttributeValue


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('id', '_name', 'is_active', 'creation_date', 'update_date')
    search_fields = ('product__brand__name', 'product__category__name', 'product__model__name')
    list_filter = ('is_active', 'option')
    readonly_fields = ('id',)

    def _name(self, obj):
        return obj.__str__()
    _name.short_description = 'Descrição'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'bar_code', 'is_active', 'creation_date', 'update_date')
    search_fields = ('name', 'brand__name', 'category__name', 'model__name')
    list_filter = ('is_active',)
    inlines = [VariantProductInline, ProductImageInline]

    def get_inline_instances(self, request, obj=None):
        inline_instances = []
        for inline_class in self.inlines:
            if inline_class is ProductImageInline:
                if obj and obj.format_type != 'with_variant':
                    inline_instances.append(inline_class(self.model, self.admin_site))

            elif inline_class is VariantProductInline:
                if obj and obj.format_type != 'simple':
                    inline_instances.append(inline_class(self.model, self.admin_site))

            else:
                inline_instances.append(inline_class(self.model, self.admin_site))

        return inline_instances


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
   


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('value',)
    search_fields = ('value',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


