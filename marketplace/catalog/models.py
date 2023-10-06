from django.db import models

def category_image_directory_path(instance: "CategoryImage", filename: str) -> str:
    if instance.category.subcategories:
        return "catalog/{category_parent}/{category}/images/{filename}".format(
            category_parent=instance.category.subcategories,
            category=instance.category,
            filename=filename,
        )
    else:
        return "catalog/{category}/icons/{filename}".format(
            category=instance.category,
            filename=filename,
        )

class Categories(models.Model):
    title = models.CharField(max_length=100, blank=True, db_index=True)
    image = models.ForeignKey("CategoryImage", on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, related_name="subcategories")

class CategoryImage(models.Model):
    src = models.FileField(upload_to=category_image_directory_path)
    alt = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, related_name="images")
