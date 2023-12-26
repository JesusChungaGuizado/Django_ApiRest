from rest_framework import serializers
from ....core.entities.users import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=  User
        fields='__all__'