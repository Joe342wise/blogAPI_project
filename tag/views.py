from django.shortcuts import render
from rest_framework import viewsets
from tag.models import TagTable as Tag
from tag.serializers import TagSerializer

# Create your views here.
class TagViewSet(viewsets.ModelViewSet):
    queryset= Tag.objects.all()
    serializer_class= TagSerializer
