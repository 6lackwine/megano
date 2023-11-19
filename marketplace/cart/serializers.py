from rest_framework import serializers

from products.models import Product, Sale
from products.serializers import TagSerializers, ProductImageSerializers, ProductSerializers


class BasketSerializer(serializers.ModelSerializer):
    super(ProductSerializers)
    price = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()
    images = ProductImageSerializers(many=True)
    # tags = TagSerializers(many=True)
    # reviews = serializers.IntegerField(source="reviews.count")
    class Meta:
        model = Product
        fields = "id", "category", "price", "count", "date", "title", "description", \
            "freeDelivery", "images", "tags", "reviews", "rating"

    def get_price(self, instance):
        saleProduct = Sale.objects.filter(product_id=instance.pk)
        salePrice = [i.salePrice for i in saleProduct]
        if salePrice:
            instance.price = salePrice[0]
            #instance.save()
            #return salePrice[0]
        return instance.price

    def get_count(self, obj):
        return self.context.get(str(obj.pk)).get('quantity')