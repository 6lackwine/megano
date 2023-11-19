from django.contrib import admin

from catalog.models import Categories, CategoryImage


class CategoryImageInline(admin.StackedInline):
    model = CategoryImage

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoryImageInline,
    ]
    list_display = "pk", "title", "parent"
    fieldsets = [
        (None, {
            "fields": ("title", "parent")
        }),
    ]
    search_fields = ["title", "parent__title"]