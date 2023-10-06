from django.urls import path

from orders.views import OrderHistoryAPIView, OrderAPIView

urlpatterns = [
    path("orders/", OrderHistoryAPIView.as_view(), name="orders_history"),
    path("orders/<int:pk>/", OrderAPIView.as_view(), name="orders_id"),
]