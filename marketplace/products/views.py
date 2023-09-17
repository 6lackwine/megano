from django.shortcuts import render
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializers


class ProductDetail(APIView):
    def get(self, request: Request, pk) -> Response:
        product = Product.objects.all()
        serialized = ProductSerializers(product, many=True)
        return Response({"products": serialized.data})

# class ProductDetail(ListModelMixin, GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
#     def get(self, request: Request, pk) -> Response:
#         return self.list(request, pk)