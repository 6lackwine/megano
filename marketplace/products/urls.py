from django.urls import path

from products.views import ProductDetail

urlpatterns = [
    path("api/product/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
]