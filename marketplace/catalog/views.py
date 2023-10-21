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
from catalog.serializers import CategoriesSerializers, CustomPagination, BasketSerializers
from products.models import Product
from products.serializers import ProductSerializers, ProductsPopularAndLimitedSerializers


class CategoryAPIView(APIView):
    def get(self, request: Request) -> Response:
        category = Categories.objects.filter(parent__isnull=True)
        serialized = CategoriesSerializers(category, many=True)
        return Response(serialized.data)

class CatalogAPIView(ListAPIView):
    serializer_class = ProductSerializers
    pagination_class = CustomPagination
    filterset_class = ProductFilter
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
            category = self.request.META['HTTP_REFERER'].split('/')[4]
            print(self.request.query_params)
            if category:
                categories = [obj.pk for obj in Categories.objects.filter(parent_id=category)]
                categories.append(int(category))
                queryset = queryset.filter(category__in=categories)
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
            if tags:
                queryset = queryset.filter(tags__in=tags)

            sort = self.request.query_params.get("sort")
            sortType = self.request.query_params.get("sortType")
            if sort == "price":
                if sortType == "inc":
                    queryset = queryset.order_by("-price")
                else:
                    queryset = queryset.order_by("price")
            elif sort == "rating":
                if sortType == "inc":
                    queryset = queryset.order_by("-rating")
                else:
                    queryset = queryset.order_by("rating")
            elif sort == "reviews":
                if sortType == "inc":
                    queryset = queryset.order_by("-reviews")
                else:
                    queryset = queryset.order_by("reviews")
            elif sort == "date":
                if sortType == "inc":
                    queryset = queryset.order_by("-date")
                else:
                    queryset = queryset.order_by("date")
            return queryset

class BasketGETAPIView(APIView):
    def get(self, request: Request):
        queryset = Product.objects.all()
        serializer = ProductsPopularAndLimitedSerializers(queryset, many=True)
        return Response(serializer.data)