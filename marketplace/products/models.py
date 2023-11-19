from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe

from catalog.models import Categories

class Product(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Категория")
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, blank=False, verbose_name="Цена")
    count = models.IntegerField(default=0, blank=False, verbose_name="Количество")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    title = models.CharField(max_length=100, blank=False, db_index=True, verbose_name="Название")
    description = models.CharField(max_length=100, blank=True, verbose_name="Описание")
    fullDescription = models.TextField(blank=True, verbose_name="Полное описание")
    freeDelivery = models.BooleanField(default=True, verbose_name="Бесплатная доставка")
    image = models.ForeignKey("ProductImage", on_delete=models.CASCADE, null=True, verbose_name="Изображение")
    tag = models.ManyToManyField("Tag", verbose_name="Тег")
    review = models.ForeignKey("Review", on_delete=models.CASCADE, null=True, verbose_name="Отзыв")
    specification = models.ForeignKey("ProductSpecification", on_delete=models.CASCADE, null=True, verbose_name="Характеристика")
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=2, verbose_name="Рейтинг")
    available = models.BooleanField(default=True, verbose_name="Наличие")
    limited = models.BooleanField(default=True, verbose_name="Лимитированный товар")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

def product_image_directory_path(instance: "ProductImage", filename: str) -> str:
    return "product/product_{pk}/images/{filename}".format(
        pk=instance.products.pk,
        filename=filename,
    )

class ProductImage(models.Model):
    src = models.FileField(upload_to=product_image_directory_path, verbose_name="Путь")
    alt = models.CharField(max_length=100, verbose_name="Название")
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="images")

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображение товаров"

    def __str__(self):
        return str(self.src)

class Review(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=30, verbose_name="Автор")
    email = models.EmailField(max_length=100)
    text = models.TextField(blank=True, verbose_name="Текст")
    rate = models.IntegerField(default=0, verbose_name="Рейтинг")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    products = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, related_name="reviews", verbose_name="Товар")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    def __str__(self):
        return f"Отзыв номер {self.pk}"

class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name="Название")
    products = models.ManyToManyField(Product, related_name="tags", verbose_name="Товар")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name

class ProductSpecification(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="specifications", verbose_name="Товар")
    name = models.CharField(max_length=100, verbose_name="Наименование")
    value = models.CharField(max_length=100, verbose_name="Значение")

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"

    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    dateFrom = models.DateField(auto_now_add=False, verbose_name="Действует до")
    dateTo = models.DateField(auto_now_add=False, verbose_name="Действует с")
    salePrice = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Цена со скидкой")

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"

    def __str__(self):
        return f"{self.product}"

    def price(self):
        return self.product.price
    def title(self):
        return self.product.title