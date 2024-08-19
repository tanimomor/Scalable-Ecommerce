# discounts/models.py

from django.db import models
from products.models import Product

class Discount(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, related_name='discounts')

    def __str__(self):
        return self.code
