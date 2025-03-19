from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer  # Define o serializer a ser utilizado
    permission_classes = [permissions.IsAuthenticated]  # Garante que apenas usuários autenticados acessem
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]  # Permite uso de filtros e busca nos endpoints
    filterset_fields = ['status', 'category']  # Campos que podem ser filtrados com ?status=...&category=...
    search_fields = ['name', 'description']  # Campos que podem ser pesquisados com ?search=...

    def get_queryset(self):
        # Retorna apenas os itens do usuário autenticado
        return Item.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Define automaticamente o usuário autenticado como dono do item
        serializer.save(owner=self.request.user)