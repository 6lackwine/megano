import csv

from django.contrib import admin
from django.db.models import QuerySet
from django.db.models.options import Options
from django.http import HttpRequest, HttpResponse

from products.models import Product, ProductImage


class ExportCSVMixin:
    def export_csv(self, request: HttpRequest, queryset: QuerySet):
        meta: Options = self.model._meta
        fields_names = [field.name for field in meta.fields] # Список из строк с названиями полей в модели

        response = HttpResponse(content_type="text/csv") # Нужен чтобы записывать в него результат
        response["Content-Disposition"] = f"attachment; filename={meta}-export.csv" # Чтобы файл можно было скачать
        csv_writer = csv.writer(response)  # Записываем результат в ответ
        csv_writer.writerow(fields_names)  # Записываем заголовки

        for obj in queryset: # Записываем все поля моделей в строчку
            csv_writer.writerow([getattr(obj, field)for field in fields_names])

        return response

        export_csv.short_description = "Export as CSV"

class ProductInline(admin.StackedInline):
    model = ProductImage

class OrderInline(admin.TabularInline):
    model = Product.orders.through

@admin.action(description="Archive products") # Указываем что данная функция является Action
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet): # queryset запрос в котором содержатся те сущности которые выбраны
    queryset.update(archived=True) # Действие которое выполнит архивацию продуктов

@admin.action(description="Unarchive products")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv", # Указываем имя действия
    ]
    inlines = [
        OrderInline,
        ProductInline,
    ]
    list_display = "pk", "title", "price"
    list_display_links = "pk", "title"
    ordering = "-title", "pk"
    search_fields = "title", "price"
    fieldsets = [
        (None, {
            "fields": ("title", "description")
        }),
        ("Price options", {
            "fields": ("price",)
        }),
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."