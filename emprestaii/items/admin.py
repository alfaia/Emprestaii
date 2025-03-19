from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'owner')  # Campos exibidos na listagem do admin
    search_fields = ('name', 'description', 'category')  # Campos pesquisáveis no admin
    list_filter = ('status', 'category')  # Filtros laterais por status e categoria
    autocomplete_fields = ['owner']  # Campo com preenchimento automático para facilitar seleção do usuário

