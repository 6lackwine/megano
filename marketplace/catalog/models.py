from django.db import models

def category_image_directory_path(instance: "CategoryImage", filename: str) -> str:
    if instance.category.parent:
        return "catalog/{category_parent}/{category}/images/{filename}".format(
            category_parent=instance.category.parent,
            category=instance.category,
            filename=filename,
        )
    else:
        return "catalog/{category}/icons/{filename}".format(
            category=instance.category,
            filename=filename,
        )

class Category(models.Model):
    class Meta:
        ordering = ["pk", "title"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="subcategories")

class CategoryImage(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name="images")
    src = models.FileField(upload_to=category_image_directory_path)