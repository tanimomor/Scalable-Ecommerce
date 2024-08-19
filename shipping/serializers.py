# shipping/serializers.py

from rest_framework import serializers
from .models import ShippingAddress

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
