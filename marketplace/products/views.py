from datetime import datetime

from rest_framework.generics import ListAPIView, GenericAPIView, CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from catalog.serializers import CustomPagination
from products.models import Product, Tag, Review, Sale
from products.serializers import TagSerializers, ProductSerializers, ReviewSerializers, \
    ProductsPopularAndLimitedSerializers, SalesSerializers


class ProductDetail(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductsPopular(APIView):
    def get(self, request: Request):
        queryset = Product.objects.order_by("title", "id")[:8]
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
        queryset = Product.objects.order_by("?")[:3]
        serializer = ProductsPopularAndLimitedSerializers(queryset, many=True)
        return Response(serializer.data)

class TagsList(APIView):
    def get(self, request: Request) -> Response:
        tag = Tag.objects.all()
        serialized = TagSerializers(tag, many=True)
        return Response(serialized.data)

class ReviewCreate(CreateModelMixin, GenericAPIView):
    # serializer_class = ReviewSerializers
    permission_classes = [IsAuthenticated]
    def post(self, request: Request, pk):
        product = Product.objects.get(pk=pk)
        Review.objects.create(
            author=request.data["author"],
            email=request.data["email"],
            text=request.data["text"],
            rate=request.data["rate"],
            #date=datetime.now(),
            products_id=product.pk,
        )
        review = [{
            "author": request.data["author"],
            "email": request.data["email"],
            "text": request.data["text"],
            "rate": request.data["rate"],
            "date": datetime.now()
        }]
        product.save()
        return Response(review)