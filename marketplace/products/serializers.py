from rest_framework import serializers

from catalog.serializers import CategoriesSerializers
from products.models import Product, Tag, ProductSpecification, Review, ProductImage


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "author", "email", "text", "rate", "date"

class SpecificationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = "name", "value"

class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "src", "alt"


class ProductSerializers(serializers.ModelSerializer):
    images = ProductImageSerializers(many=True)
    tags = TagSerializers(many=True)
    reviews = ReviewSerializers(many=True)
    specifications = SpecificationsSerializers(many=True)

    # def get_tags(self, instance: Product):
    #     tags = [{
    #         "id": tag.id,
    #         "name": tag.name
    #     }
    #         for tag in instance.tags.all()
    #     ]
    #     return tags
    class Meta:
        model = Product
        fields = "id", "category", "price", "count", "date", "title", "description", \
            "fullDescription", "freeDelivery", "images", "tags", "reviews", "specifications", "rating"