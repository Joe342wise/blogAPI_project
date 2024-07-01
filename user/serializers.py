from rest_framework import serializers
from user.models import UserTable as user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'
