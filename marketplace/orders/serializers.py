from rest_framework import serializers

from orders.models import Order
from products.serializers import ProductSerializers


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializers(many=True)
    class Meta:
        model = Order
        fields = "id", "createdAt", "fullName", "email", "phone", "deliveryType", \
            "paymentType", "totalCost", "status", "city", "address", "products"