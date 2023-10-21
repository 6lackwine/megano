from rest_framework import serializers

from catalog.serializers import CategoriesSerializers
from products.models import Product, Tag, ProductSpecification, Review, ProductImage, Sale


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name",)

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "author", "email", "text", "rate", "date"

class ReviewPOSTSerializers(serializers.ModelSerializer):
    author = serializers.CharField(max_length=100)
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

class ProductsPopularAndLimitedSerializers(serializers.ModelSerializer):
    price = serializers.FloatField()
    #date = serializers.DateTimeField()
    images = ProductImageSerializers(many=True)
    tags = TagSerializers(many=True)
    reviews = serializers.IntegerField(source="reviews.count")
    rating = serializers.FloatField()
    class Meta:
        model = Product
        fields = "id", "category", "price", "count", "date", "title", "description", \
            "freeDelivery", "images", "tags", "reviews", "rating"

class SalesSerializers(serializers.ModelSerializer):
    price = serializers.StringRelatedField()
    title = serializers.StringRelatedField()
    images = serializers.SerializerMethodField()
    dateFrom = serializers.DateTimeField()
    dateTo = serializers.DateTimeField()

    def get_images(self, instance):
        images = []
        images_tmp = instance.product.images.all()
        for image in images_tmp:
            images.append({"src": f"{image.src}", "alt": image.alt})
        return images

    class Meta:
        model = Sale
        fields = "id", "price", "salePrice", "dateFrom", "dateTo", "title", "images",
