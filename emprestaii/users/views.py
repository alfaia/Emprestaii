from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

# Importação dos modelos e serializers usados nas views
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer
from .serializers import CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    # Define o queryset base (não usado diretamente aqui, mas necessário)
    queryset = CustomUser.objects.all()

    # Serializer que será utilizado para validar e criar o novo usuário
    serializer_class = RegisterSerializer

    # Permite que qualquer pessoa (mesmo não autenticada) acesse essa view
    permission_classes = [permissions.AllowAny]


class ProfileView(generics.RetrieveUpdateAPIView):
    # Serializer que será usado para exibir e atualizar os dados do usuário
    serializer_class = UserSerializer

    # Permite acesso apenas a usuários autenticados (com JWT válido)
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Retorna o próprio usuário logado (request.user) como objeto da view
        return self.request.user

    
class CustomTokenObtainPairView(TokenObtainPairView):
    # Substitui o serializer padrão pelo nosso personalizado (que aceita email como login)
    serializer_class = CustomTokenObtainPairSerializer



class LogoutView(APIView):
    # Apenas usuários autenticados podem realizar logout
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            # Recupera o refresh token enviado no corpo da requisição
            refresh_token = request.data["refresh"]

            # Converte para um objeto RefreshToken e aplica blacklist
            token = RefreshToken(refresh_token)
            token.blacklist()

            # Retorna status 205 (Logout com sucesso, conteúdo resetado)
            return Response(status=status.HTTP_205_RESET_CONTENT)

        except Exception:
            # Em caso de erro (ex: token inválido), retorna erro 400
            return Response(status=status.HTTP_400_BAD_REQUEST)

