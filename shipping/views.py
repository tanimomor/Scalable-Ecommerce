# shipping/views.py

from rest_framework import viewsets
from .models import ShippingAddress
from .serializers import ShippingAddressSerializer

class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
