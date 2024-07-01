from rest_framework import serializers
from category.models import CategoryTable as category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'
        