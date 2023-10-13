from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination

from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from catalog.filters import ProductFilter
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
    serializer_class = ProductSerializers
    pagination_class = CustomPagination
    #filterset_class = ProductFilter
    filter_backends = (DjangoFilterBackend,)
    def get_queryset(self):
        queryset = Product.objects.all()
        if self.request.query_params:
            name = self.request.query_params.get("filter[name]")
            minPrice = self.request.query_params.get("filter[minPrice]")
            maxPrice = self.request.query_params.get("filter[maxPrice]")
            freeDelivery = self.request.query_params.get("filter[freeDelivery]")
            available = self.request.query_params.get("filter[available]")
            tags = self.request.query_params.getlist('tags[]')
            print(self.request.query_params, "AAAAAAA")
            if name:
                queryset = queryset.filter(title__icontains=name)
            if minPrice:
                queryset = queryset.filter(price__gte=minPrice)
            if maxPrice:
                queryset = queryset.filter(price__lte=maxPrice)
            if freeDelivery and freeDelivery == "true":
                queryset = queryset.filter(freeDelivery=True)
            if available == "true":
                queryset = queryset.filter(available=True)
            if len(tags) != 0:
                queryset = queryset.filter(tags__in=tags)
            return queryset