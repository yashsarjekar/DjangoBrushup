from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('users/', views.UserCreateView.as_view(), name='users'),
]