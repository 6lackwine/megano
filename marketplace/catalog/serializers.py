from rest_framework import serializers, pagination
from rest_framework.response import Response

from catalog.models import Categories, CategoryImage


class CategoryImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = "src", "alt"

class SubcategoriesSerializers(serializers.ModelSerializer):
    image = CategoryImageSerializers()
    class Meta:
        model = Categories
        fields = "id", "title", "image"

class CategoriesSerializers(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    image = CategoryImageSerializers()
    subcategories = SubcategoriesSerializers(many=True)
    # subcategories = serializers.SerializerMethodField()

    # def get_subcategories(self, obj):
    #     queryset = Categories.objects.filter(subcategories=obj)
    #     if obj.subcategories is None:
    #         return [CategoriesSerializers(q).data for q in queryset]
    #     return CategoriesSerializers(queryset, many=True).data
    class Meta:
        model = Categories
        fields = "id", "title", "image", "subcategories"

class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 1000
    page_query_param = "page_size"
    def get_paginated_response(self, data):
        return Response({
            'items': data,
            "currentPage": self.page.number,
            "lastPage": self.page.paginator.num_pages,
        })