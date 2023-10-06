from django.db import models

from products.models import Product
from profiles.models import Profiles


class Order(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    deliveryType = models.CharField(max_length=100)
    paymentType = models.CharField(max_length=100)
    totalCost = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    products = models.ManyToManyField(Product, related_name="orders")
