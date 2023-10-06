from django.shortcuts import render
from rest_framework import pagination

from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from catalog.models import Categories
from catalog.serializers import CategoriesSerializers, CustomPagination
from products.models import Product
from products.serializers import ProductSerializers


class CategoryAPIView(APIView):
    def get(self, request: Request) -> Response:
        category = Categories.objects.filter(parent__isnull=True)
        serialized = CategoriesSerializers(category, many=True)
        return Response(serialized.data)

class CatalogAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    pagination_class = CustomPagination
    filterset_fields = [
        "title",
        "price",
        "freeDelivery",
    ]