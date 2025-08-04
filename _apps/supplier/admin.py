from django.contrib import admin

from .models import Supplier

@admin.register(Supplier)
class SuplierAdmin(admin.ModelAdmin):
    model = Supplier
    list_display = ('id', 'name', 'email', 'cnpj', 'creation_date', 'is_active')
    search_fields = ('id', 'name', 'email', 'cnpj')

