from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.serializers.user_serializers import UserSerializer

# Create your views here.
class UserLoginView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful'})
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as err:
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

class UserCreateView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(err, status=status.HTTP_400_BAD_REQUEST)
