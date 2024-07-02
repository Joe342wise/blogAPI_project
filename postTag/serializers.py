from rest_framework import serializers
from postTag.models import PostTagTable as PostTag

class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = '__all__'