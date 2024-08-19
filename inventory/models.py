# inventory/models.py

from django.db import models
from products.models import Product

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return f"Inventory for {self.product.name}"
