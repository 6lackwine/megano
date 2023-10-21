from django.urls import path

from catalog.views import CategoryAPIView, CatalogAPIView, BasketGETAPIView

urlpatterns = [
    path("categories/", CategoryAPIView.as_view(), name="categories"),
    path("catalog/", CatalogAPIView.as_view(), name="catalog_list"),
    path("basket/", BasketGETAPIView.as_view(), name="basket"),
]