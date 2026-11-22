from rest_framework import serializers
from .models import DealerProfile

class DealerProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = DealerProfile
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']

class DealerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerProfile
        fields = [
            'id',
            'shop_name',
            'owner_name',
            'phone_number',
            'address',
            'city',
            'latitude',
            'longitude',
        ]