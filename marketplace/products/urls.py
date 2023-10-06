from django.urls import path

from products.views import TagsList, ProductDetail

urlpatterns = [
    path("product/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    #path("product/<int:pk>/review", ReviewCreate.as_view(), name="create_review"),
    path("tags/", TagsList.as_view(), name="tags_list"),
]