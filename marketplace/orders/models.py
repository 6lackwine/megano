from django.db import models

from products.models import Product
from profiles.models import Profile


class Order(models.Model):
    class Meta:
        ordering = ["pk", "createdAt", "status"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    address = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="orders")
    deliveryType = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    paymentType = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name="orders")
    totalCost = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
