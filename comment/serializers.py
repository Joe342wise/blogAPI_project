from rest_framework import serializers
from comment.models import CommentTable as Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'