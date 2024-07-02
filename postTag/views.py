from django.shortcuts import render
from rest_framework import viewsets
from postTag.models import PostTagTable as PostTag
from postTag.serializers import PostTagSerializer

# Create your views here.
class PostTagView(viewsets.ModelViewSet):
    queryset = PostTag.objects.all()
    serializer_class = PostTagSerializer
