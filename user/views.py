from django.shortcuts import render
from rest_framework import viewsets
from user.models import UserTable as user
from user.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
