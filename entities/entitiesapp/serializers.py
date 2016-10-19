from rest_framework import serializers
from entitiesapp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'username', 'user_type', 'date_created', 'date_of_birth',
            'income', 'city', 'state', 'password'
        )
