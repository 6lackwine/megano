from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView

from cart.cart import Cart
from orders.models import Order, ProductOrderCount
from orders.serializers import OrderSerializer
from products.models import Product
from profiles.models import Profiles


class OrderAPIView(APIView):
    def get(self, request: Request):
        order = Order.objects.filter(user_id=request.user.users.pk).order_by("-createdAt")
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        profile = Profiles.objects.get(user=request.user.pk)
        products_in_order = [
            (
                product["id"],
                product["count"],
                product["price"]
            )
            for product in request.data
        ]
        products = Product.objects.filter(id__in=[product[0] for product in products_in_order])
        order = Order.objects.create(
            user=profile,
            totalCost=Cart(request).get_total_price(),
        )
        data = {
            "orderId": order.pk,
        }
        order.products.set(products)
        order.save()
        return Response(data)

class OrderIDAPIView(APIView):
    def get(self, request: Request, pk):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        cart = Cart(request).cart
        try:
            products_in_order = order.products
            query = ProductOrderCount.objects.filter(order_id=order.pk)
            count_products = {product.products.pk: product.count for product in query}
            for count_product in products_in_order.all():
                count_product.count = count_products[count_product.pk]
        except:
            products_in_order = order.products
            for count_product in products_in_order.all():
                count_product.count = cart[str(count_product.pk)]["quantity"]
                count_product.save()
        return Response(serializer.data)

    def post(self, request: Request, pk):
        print(request.data)
        order = Order.objects.get(pk=pk)
        order.fullName = request.data["fullName"]
        order.phone = request.data["phone"]
        order.email = request.data["email"]
        order.city = request.data["city"]
        order.address = request.data["address"]
        order.paymentType = request.data["paymentType"]
        order.status = "Ожидает оплаты"
        order.deliveryType = request.data["deliveryType"]
        if order.deliveryType == "express":
            order.totalCost += 500
        else:
            if order.totalCost < 2000:
                # if request.data["totalCost"] < 2000:
               order.totalCost += 200

        for product in request.data["products"]:
            ProductOrderCount.objects.get_or_create(
                order_id=order.pk,
                products_id=product["id"],
                count=product["count"],
            )

        data = {
            "orderId": order.pk,
        }
        order.save()
        Cart(request).clear()
        return Response(data, status=200)

class PaymentAPIView(APIView):
    def post(self, request, pk):
        order = Order.objects.get(pk=pk)
        number = request.data["number"]
        print(request.data)
        print(order.paymentType)
        # if order.paymentType == "online":
        print(int(number.split()[3][3]))
        if len(number) == 19 and int(number.split()[3]) % 2 == 0 and int(number.split()[3][3]) != 0:
            order.status = "Оплачено"
        else:
            order.status = "Ошибка оплаты, недостаточно средств"
        # elif order.paymentType == "someone":
        #     print(request.data)
        #     if len(number) == 7 and int(number.split()[3]) % 2 == 0 and int(number.split()[3][3]) != 0:
        #         order.status = "Оплачено"
        #     else:
        #         order.status = "Ошибка оплаты, недостаточно средств"
        order.save()
        return Response(status=200)