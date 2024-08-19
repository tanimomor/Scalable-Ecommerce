# discounts/views.py

from rest_framework import viewsets
from .models import Discount
from .serializers import DiscountSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
