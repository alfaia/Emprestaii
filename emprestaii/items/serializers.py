from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item  # Modelo associado ao serializer
        fields = ['id', 'name', 'description', 'category', 'status', 'owner']  # Campos que serão serializados
        read_only_fields = ['owner']  # Campo somente leitura (preenchido automaticamente com o usuário autenticado)