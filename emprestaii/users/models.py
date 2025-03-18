# Importa o AbstractUser (modelo base para sobrescrever User padrão do Django)
# e o BaseUserManager (classe para criar usuários/superusuários com lógica customizada)
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Verifica se o campo de email foi informado
        if not email:
            raise ValueError("The Email field is required.")
        
        # Normaliza o email (tudo minúsculo, remove espaços etc.)
        email = self.normalize_email(email)

        # Cria a instância do usuário com email e campos extras
        user = self.model(email=email, **extra_fields)

        # Criptografa e define a senha do usuário
        user.set_password(password)

        # Salva o usuário no banco de dados
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Define permissões obrigatórias para superusuário
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # Cria superusuário usando o método acima
        return self.create_user(email, password, **extra_fields)


class Address(models.Model):
    street = models.CharField(max_length=100)        # Nome da rua
    number = models.IntegerField()                   # Número da casa/apartamento
    neighborhood = models.CharField(max_length=100)  # Bairro
    city = models.CharField(max_length=100)          # Cidade

    def __str__(self):
        # Retorna a representação textual do endereço
        return f"{self.street}, {self.number}, {self.neighborhood}, {self.city}"



class CustomUser(AbstractUser):
    # Campo de email obrigatório e único, agora usado como identificador de login
    email = models.EmailField(
        max_length=100, 
        unique=True, 
        blank=False, 
        null=False
    )

    # Campo username agora é opcional (mas ainda existe, se quiser usar no futuro)
    username = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        unique=True
    )

    # Nome completo do usuário
    name = models.CharField(max_length=100)

    # Telefone de contato, não obrigatório
    phone = models.CharField(max_length=20, blank=True, null=True)

    # Relacionamento OneToOne com o modelo Address (um usuário → um endereço)
    address = models.OneToOneField(
        Address, 
        on_delete=models.SET_NULL,  # Se o endereço for apagado, o campo vira NULL
        blank=True,
        null=True
    )

    # Define que o login será feito usando o campo email (não mais o username padrão)
    USERNAME_FIELD = 'email'

    # Remove exigência de campos obrigatórios adicionais no createsuperuser
    REQUIRED_FIELDS = []

    # Define o manager personalizado criado acima para criar usuários corretamente
    objects = CustomUserManager()

    def __str__(self):
        # Retorna o email como representação textual do usuário
        return self.email
