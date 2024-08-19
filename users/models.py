from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)

    CUSTOMER = 'customer'
    SELLER = 'seller'
    ADMIN = 'admin'
    USER_TYPE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (SELLER, 'Seller'),
        (ADMIN, 'Admin'),
    ]

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default=CUSTOMER,
    )

    def is_customer(self):
        return self.user_type == self.CUSTOMER

    def is_seller(self):
        return self.user_type == self.SELLER

    def is_admin(self):
        return self.user_type == self.ADMIN

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)
    store_description = models.TextField()