from django.contrib.auth.models import User
from django.db import models

from catalog.models import Categories

class Product(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=False)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, blank=False)
    count = models.IntegerField(default=0, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    fullDescription = models.CharField(max_length=100, blank=True)
    freeDelivery = models.BooleanField(default=True)
    image = models.ForeignKey("ProductImage", on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField("Tag")
    review = models.ForeignKey("Review", on_delete=models.CASCADE, null=True)
    specification = models.ForeignKey("ProductSpecification", on_delete=models.CASCADE, null=True)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=2)

def product_image_directory_path(instance: "ProductImage", filename: str) -> str:
    return "product/product_{pk}/images/{filename}".format(
        pk=instance.products.pk,
        filename=filename,
    )

class ProductImage(models.Model):
    src = models.FileField(upload_to=product_image_directory_path)
    alt = models.CharField(max_length=100)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="images")

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    text = models.TextField(blank=True)
    rate = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, related_name="reviews")

class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True)
    products = models.ManyToManyField(Product, related_name="tags")

class ProductSpecification(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="specifications")
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    dateFrom = models.DateField(auto_now_add=True)
    dateTo = models.DateField(auto_now_add=True)
    salePrice = models.DecimalField(max_digits=8, decimal_places=2, default=0)