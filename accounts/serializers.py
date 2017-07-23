from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'photo', 'birthday')

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate(self, attrs):
        if 'a' in attrs.get('username'):
            raise serializers.ValidationError('not allowed symbol')

        return attrs