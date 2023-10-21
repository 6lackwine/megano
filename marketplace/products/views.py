from datetime import datetime
from django.db.models import Count

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, GenericAPIView, CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from catalog.serializers import CustomPagination
from products.models import Product, Tag, Review, Sale
from products.serializers import TagSerializers, ProductSerializers, ReviewSerializers, \
    ProductsPopularAndLimitedSerializers, \
    ReviewPOSTSerializers, SalesSerializers


class ProductDetail(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductsPopular(APIView):
    def get(self, request: Request):
        queryset = Product.objects.all()[:8]
        serializer_class = ProductsPopularAndLimitedSerializers(queryset, many=True)
        return Response(serializer_class.data)

class ProductsLimited(APIView):
    def get(self, request: Request):
        queryset = Product.objects.filter(limited=True)[:16]
        serializer_class = ProductsPopularAndLimitedSerializers(queryset, many=True)
        return Response(serializer_class.data)

class SalesAPIView(ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SalesSerializers
    pagination_class = CustomPagination

class BannersAPIView(APIView):
    def get(self, request: Request):
        queryset = Product.objects.all()
        serializer = ProductsPopularAndLimitedSerializers(queryset, many=True)
        return Response(serializer.data)

class TagsList(APIView):
    def get(self, request: Request) -> Response:
        tag = Tag.objects.all()
        serialized = TagSerializers(tag, many=True)
        return Response(serialized.data)

# class ReviewCreate(ListCreateAPIView):
#     serializer_class = ReviewSerializers
#     queryset = Review.objects.all()
#     def post(self, request, *args, **kwargs):
#         if request.method == "POST":
#             return self.create(request, *args, **kwargs)

# class ReviewCreate(CreateModelMixin, GenericAPIView):
#     serializer_class = ReviewSerializers
#     def post(self, request: Request, pk):
#         product = Product.objects.get(pk=pk)
#         #request.data["product"] = product.pk
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         Review.objects.create(author_id=request.data['author'], email=request.data['email'],
#                               text=request.data['text'], rate=request.data['rate'],
#                               date=datetime.now(), products_id=product.pk)
#
#         reviews = Review.objects.filter(products_id=product.pk)
#         summa = sum([obj.rate for obj in reviews])
#         product.rating = summa / len(reviews)
#         product.save()
#
#         return Response(request.data)
class ReviewCreate(CreateModelMixin, GenericAPIView):
    serializer_class = ReviewPOSTSerializers
    def post(self, request: Request, pk):
        product = Product.objects.get(pk=pk)
        Review.objects.create(
            author_id=request.data["author"],
            email=request.data["email"],
            text=request.data["text"],
            rate=request.data["rate"],
            date=datetime.now(),
            products_id=product.pk,
        )
        review = {
            "author": request.data["author"],
            "email": request.data["email"],
            "text": request.data["text"],
            "rate": request.data["rate"],
            "date": datetime.now()
        }
        product.save()
        return Response(review)