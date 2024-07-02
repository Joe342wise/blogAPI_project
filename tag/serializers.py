from rest_framework import serializers
from tag.models import TagTable as Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'