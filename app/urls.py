# project_name/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from users.views import UserViewSet, CustomerProfileViewSet, SellerProfileViewSet
from products.views import ProductViewSet, CategoryViewSet
from orders.views import OrderViewSet, OrderItemViewSet
from cart.views import CartViewSet, CartItemViewSet
from payments.views import PaymentViewSet
from reviews.views import ReviewViewSet
from shipping.views import ShippingAddressViewSet
from discounts.views import DiscountViewSet
from inventory.views import InventoryViewSet
from notifications.views import NotificationViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'customers', CustomerProfileViewSet)
router.register(r'sellers', SellerProfileViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'shipping-addresses', ShippingAddressViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('auths.urls')),  # Include auth URLs
]
