from rest_framework import serializers
from posts.models import PostTable as Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' #('id', 'title', 'content', 'created_at', 'updated_at')
        
