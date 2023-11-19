import datetime

from rest_framework import serializers

from orders.models import Order
from products.serializers import ProductSerializers


class OrderSerializer(serializers.ModelSerializer):
    createdAt = serializers.SerializerMethodField()
    products = ProductSerializers(many=True)
    class Meta:
        model = Order
        fields = "id", "createdAt", "fullName", "email", "phone", "deliveryType", \
            "paymentType", "totalCost", "status", "city", "address", "products"

    def get_createdAt(self, instance):
        date = instance.createdAt + datetime.timedelta(hours=3)
        return datetime.datetime.strftime(date, '%d.%m.%Y %H:%M')