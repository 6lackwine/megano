from django.contrib import admin

from catalog.models import Categories, CategoryImage

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "parent"
    fieldsets = [
        (None, {
            "fields": ("title", "parent", "image")
        }),
    ]
    search_fields = ["title", "parent__title"]

@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
    list_display = "pk", "src", "alt", "category"
    fieldsets = [
        (None, {
            "fields": ("src", "alt", "category")
        })
    ]
    search_fields = ["alt", "src", "category__title"]