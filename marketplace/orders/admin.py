from django.contrib import admin

from orders.models import Order, ProductOrderCount
from products.models import Product


class ProductOrderCountInline(admin.TabularInline):
    model = ProductOrderCount

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductOrderCountInline,
    ]
    list_display = "id", "user", "createdAt", "fullName", "email", "phone", "deliveryType",\
        "paymentType", "totalCost", "status", "city", "address", "products_list"
    fieldsets = [
        (None, {
            "fields": ("user", "fullName", "email", "phone", "deliveryType",
                       "paymentType", "totalCost", "status", "city", "address")
        }),
    ]
    search_fields = ["id", "user__user__username", "fullName", "phone", "status", "city", "address"]

    def products_list(self, obj: ProductOrderCount):
        return ", ".join([b.title for b in obj.products.all()])


@admin.register(ProductOrderCount)
class ProductOrderCountAdmin(admin.ModelAdmin):
    list_display = "id", "order", "products", "count"
    ordering = ["order"]
    fieldsets = [
        (None, {
            "fields": ("order", "products", "count")
        })
    ]
