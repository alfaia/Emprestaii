from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Address, CustomUser


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'  # inclui todos os campos do modelo Address


class RegisterSerializer(serializers.ModelSerializer):
    address = AddressSerializer()  # Nested (Serializer aninhado) serializer para capturar os dados do endereço
    password = serializers.CharField(write_only=True)  # senha será enviada, mas nunca retornada no response


    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'name', 'phone', 'address']

    def create(self, validated_data):
        address_data = validated_data.pop('address')  # extrai os dados do endereço
        address = Address.objects.create(**address_data)  # cria o endereço no banco

        # cria o usuário com os demais dados (utilizando o manager `create_user`)
        user = CustomUser.objects.create_user(
            username=validated_data.get('username'),  # username opcional
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data.get('name'),
            phone=validated_data.get('phone'),
            address=address
        )
        return user

    

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)  # apenas leitura; não será editado diretamente por aqui


    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'name',
            'phone',
            'address'
        ]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = CustomUser.EMAIL_FIELD  # define que o campo de login será `email`

    def validate(self, attrs):
        return super().validate(attrs) # mantém validação padrão


