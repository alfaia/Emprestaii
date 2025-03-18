from django.urls import path

# Importa as views do app de usuários
from .views import (
    RegisterView, 
    ProfileView, 
    CustomTokenObtainPairView, 
    LogoutView
)

# Importa a view padrão de refresh token do SimpleJWT
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Rota de cadastro de novo usuário
    path('register/', RegisterView.as_view(), name='user-register'),
    
    # Rota para visualizar ou atualizar o perfil do usuário logado
    path('profile/', ProfileView.as_view(), name='user-profile'),
    
    # Rota de login (autenticação via email e senha, retorna tokens JWT)
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Rota para renovar o access token (usando refresh token válido)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Rota de logout (invalida o refresh token via blacklist)
    path('logout/', LogoutView.as_view(), name='user-logout'),
]
