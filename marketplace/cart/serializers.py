from rest_framework import serializers

from products.models import Product
from products.serializers import TagSerializers, ProductImageSerializers


class BasketSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    images = ProductImageSerializers(many=True)
    tags = TagSerializers(many=True)
    reviews = serializers.IntegerField(source="reviews.count")
    class Meta:
        model = Product
        fields = "id", "category", "price", "count", "date", "title", "description", \
            "freeDelivery", "images", "tags", "reviews", "rating"

    def get_count(self, obj):
        print(self.context)
        return self.context.get(str(obj.pk)).get('quantity')