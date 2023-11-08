import datetime

from rest_framework import serializers

from orders.models import Order
from products.models import Product
from products.serializers import ProductSerializers, ProductImageSerializers, TagSerializers


class ProductsOrderSerializer(serializers.ModelSerializer):
    price = serializers.FloatField()
    images = ProductImageSerializers(many=True)
    tags = TagSerializers(many=True)
    reviews = serializers.IntegerField(source="reviews.count")
    rating = serializers.FloatField()
    class Meta:
        model = Product
        fields = "id", "category", "price", "count", "date", "title", "description", \
            "freeDelivery", "images", "tags", "reviews", "rating"


class OrderSerializer(serializers.ModelSerializer):
    createdAt = serializers.SerializerMethodField()
    # totalCost = serializers.DecimalField(max_digits=)
    products = ProductsOrderSerializer(many=True)
    class Meta:
        model = Order
        fields = "id", "createdAt", "fullName", "email", "phone", "deliveryType", \
            "paymentType", "totalCost", "status", "city", "address", "products"

    def get_createdAt(self, instance):
        # return datetime.datetime.now()
        date = instance.createdAt + datetime.timedelta(hours=3)
        return datetime.datetime.strftime(date, '%d.%m.%Y %H:%M')