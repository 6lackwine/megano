from datetime import datetime

from django.shortcuts import render
from rest_framework.generics import ListAPIView, GenericAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from products.models import Product, Tag, ProductSpecification
from products.serializers import TagSerializers, ProductSerializers


class ProductDetail(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class TagsList(APIView):
    def get(self, request: Request) -> Response:
        tag = Tag.objects.all()
        serialized = TagSerializers(tag, many=True)
        return Response(serialized.data)

# class ReviewCreate(CreateModelMixin, GenericAPIView):
#     serializer_class = ReviewSerializers
#     queryset = Review.objects.all()
#     def post(self, request, *args, **kwargs):
#         if request.method == "POST":
#             review = Review.objects.all()
#             serialized = ReviewSerializers(review, many=True)
#             #request.data["date"] = datetime.now()
#             return Response(serialized.data)


# class SpecificationList(APIView):
#     def get(self, request: Request) -> Response:
#         specification = ProductSpecification.objects.all()
#         serialized = SpecificationSerializers(specification, many=True)
#         return Response(serialized.data)