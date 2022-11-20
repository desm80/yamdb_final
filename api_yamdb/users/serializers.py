from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для эндпоита users."""

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )
        lookup_field = 'username'

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Нельзя использовать имя me в качестве имени пользователя.'
            )
        return value


class TokenObtainPairSerializer(serializers.Serializer):
    """Сериализатор для эндпоита auth/token."""

    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    def validate(self, value):
        user = get_object_or_404(
            User, username=value.get('username')
        )
        if user.confirmation_code != value.get('confirmation_code'):
            raise serializers.ValidationError(
                'Некорректный код подтверждения'
            )
        refresh = RefreshToken.for_user(user)
        # data = {'access_token': str(refresh.access_token)}
        return {'access_token': str(refresh.access_token)}


class UserSignUpSerializer(serializers.Serializer):
    """Сериализатор для эндпоита auth/signup."""

    email = serializers.EmailField(max_length=254, required=True)
    username = serializers.CharField(required=True)

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Нельзя использовать имя me в качестве имени пользователя.'
            )
        return value
