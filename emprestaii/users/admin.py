from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Address

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Campos visíveis na listagem de usuários
    list_display = ['email', 'username', 'name', 'phone', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']

    # Campos buscáveis no admin
    search_fields = ['email', 'username', 'name']

    # Organização dos campos no formulário de edição
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Campos exibidos no formulário de criação de usuário (admin)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'name', 'phone', 'address', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Address)
