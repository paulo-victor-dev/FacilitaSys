from django.contrib import admin

from .models import Flow, FlowItem

class FlowItemInline(admin.TabularInline):
    model = FlowItem
    extra = 1
    fields = ('product', 'quantity')

@admin.register(Flow)
class FlowAdmin(admin.ModelAdmin):
    model = Flow

    list_display = (
        'id', 
        'flow_type', 
        'origin', 
        'destination', 
        'creation_date'
    )
    
    search_fields = ('id', 'flow_type')

    inlines = [FlowItemInline]
