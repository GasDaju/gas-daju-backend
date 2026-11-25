
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = [
            'full_name',
            'username',
            'email',
            'phone_number',
            'location',
            'password',
            'role'
        ]
        extra_kwargs = {
            'username': {'required': False},
            'full_name': {'required': True},
            'location': {'required': True},
        }

    def create(self, validated_data):
        username = validated_data.pop('username', None)

        if not username:
            username = validated_data['phone_number']

        user = User.objects.create_user(
            username=username,
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            role=validated_data['role'],
            full_name=validated_data['full_name'],
            location=validated_data['location']
        )

        return user
