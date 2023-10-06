from django.shortcuts import render, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView

from orders.models import Order
from orders.serializers import OrderSerializer

class OrderHistoryAPIView(APIView):
    def get(self, request: Request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

class OrderAPIView(APIView):
    def get(self, request: Request, pk):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)