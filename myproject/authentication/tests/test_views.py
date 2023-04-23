import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import User
from authentication.serializers.user_serializers import UserSerializer

class UserTests(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_user_login(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Login successful')

    def test_user_creation(self):
        url = reverse('users')
        data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword', 'first_name':'new', 'last_name':'user'}
        response = self.client.post(url, data, format='json')
        print(response.content)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username='newuser')
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
