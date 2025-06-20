from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    fields = ('product', 'quantity', 'unit_price', 'get_subtotal')
    readonly_fields = ('get_subtotal',) 

    def get_subtotal(self, obj):
        if obj.unit_price is None or obj.quantity is None:
            return '-'
        return obj.total
    get_subtotal.short_description = 'Subtotal'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total')
    search_fields = ('id', 'customer', 'status')
    list_filter = ('status',)
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()
    list_filter  = ()