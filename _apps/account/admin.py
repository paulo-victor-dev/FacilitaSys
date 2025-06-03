from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User

    # List fields
    list_display = ('first_name', 'email', 'user_type', 'date_joined', 'is_active')

    list_filter = ('user_type', 'is_active')

    search_fields = ('first_name', 'email', 'last_name')

    ordering = ('first_name',)

    # Read only fields
    readonly_fields = ('date_joined', 'last_login')

    # Show/Edit fields
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações do usuário', {
            'fields': ('first_name', 'last_name', 'user_type', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Datas', {'fields': ('date_joined', 'last_login')})
    )

    # Add user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'user_type', 'is_active', 'is_staff', 'is_superuser')
        }),
    )

