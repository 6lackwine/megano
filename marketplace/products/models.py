from django.contrib.auth.models import User
from django.db import models

from catalog.models import Category

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, blank=False)
    count = models.IntegerField(default=0, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    fullDescription = models.CharField(max_length=100, blank=True)
    freeDelivery = models.BooleanField(default=True)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=2)

def product_image_directory_path(instance: "ProductImage", filename: str) -> str:
    return "product/product_{pk}/images/{filename}".format(
        pk=instance.product.pk,
        filename=filename,
    )

class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=product_image_directory_path)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    email = models.EmailField(max_length=100)
    text = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    rate = models.PositiveSmallIntegerField(default=5)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True)
    product = models.ManyToManyField(Product)

class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    dateFrom = models.DateField(auto_now_add=True)
    dateTo = models.DateField(auto_now_add=True)
    salePrice = models.DecimalField(max_digits=8, decimal_places=2, default=0)
