from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')  # Registro automático do endpoint /items/ com todas as operações CRUD

urlpatterns = [
    path('', include(router.urls)),  # Inclusão das rotas geradas pelo router
]