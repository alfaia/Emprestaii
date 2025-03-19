from django.db import models
from django.conf import settings

# Modelo que representa um item pessoal cadastrado pelo usuário.
class Item(models.Model):
    # Opções de status disponíveis para o item: disponível, emprestado ou indisponível.
    STATUS_CHOICES = [
        ('available', 'Available'),  # Disponível para empréstimo ou uso
        ('borrowed', 'Borrowed'),   # Atualmente emprestado
        ('unavailable', 'Unavailable'),  # Não disponível no momento
    ]

    name = models.CharField(max_length=100)  # Nome do item
    description = models.TextField(blank=True)  # Descrição adicional sobre o item
    category = models.CharField(max_length=100)  # Categoria a que o item pertence (ex: Eletrônicos, Livros, etc)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')  # Situação atual do item
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='items')  # Usuário dono do item

    def __str__(self):
        return self.name