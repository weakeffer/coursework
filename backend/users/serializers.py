from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Users
import re

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = Users.objects.filter(email=email).first()
            if user:
                if user.check_password(password):
                    if user.is_active:
                        refresh = RefreshToken.for_user(user)
                        
                        return {
                            'user': user,
                            'tokens': {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                            }
                        }
                    else:
                        raise serializers.ValidationError({"general":"Аккаунт деактивирован"})
                else:
                    raise serializers.ValidationError({"password":"Неверный пароль"})
            else:
                raise serializers.ValidationError({"email":"Пользователь с таким email не найден"})
        else:
            raise serializers.ValidationError({"general":"Email и пароль обязательны"})

class UsersSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    email = serializers.CharField(
        max_length=50, 
        required=True,
        error_messages={
            'required': 'Поле обязательно', 
            'max_length': 'Длина не должна превышать 50 символов'
        }
    )
    name = serializers.CharField(
        max_length=15, 
        required=True,
        error_messages={
            'required': 'Поле обязательно', 
            'max_length': 'Длина не должна превышать 15 символов'
        }
    )
    password = serializers.CharField(
        max_length=128, 
        required=True, 
        write_only=True,
        error_messages={
            'required': 'Поле обязательно', 
            'max_length': 'Длина не должна превышать 128 символов'
        }
    )

    def validate_email(self, value):
        if Users.objects.filter(email=value).first():
            raise serializers.ValidationError("Пользователь с таким email уже существует")
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise serializers.ValidationError("Введите корректный email адрес")
        
        return value

    def validate_name(self, value): 
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Имя должно содержать минимум 2 символа")
        
        if not re.match(r'^[a-zA-Zа-яА-ЯёЁ\s]+$', value):
            raise serializers.ValidationError("Имя может содержать только буквы и пробелы")
        
        return value.strip()

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Пароль должен содержать минимум 8 символов")
        
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну цифру")
        
        if not any(char.isalpha() for char in value):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну букву")
        
        return value

    def create(self, validated_data):
        user = Users(
            email=validated_data['email'],
            name=validated_data['name'],
            is_active=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user