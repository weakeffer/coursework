from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Users
from rest_framework.permissions import AllowAny
from .serializers import UsersSerializer, UserLoginSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        try:
            serializer = UsersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success' : True,
                    'data' : serializer.data,
                    'message' : 'Пользователь успешно создан'
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'success': False,
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({
                'success': False,
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    serializer = UserLoginSerializer(data = request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        user = data['user']
        tokens = data['tokens']

        user_data = UsersSerializer(user).data
        return Response({
            'success': True,
            'message': 'Вход выполнен успешно',
            'user': user_data,
            'tokens': tokens
        })
    else:
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_401_UNAUTHORIZED)
