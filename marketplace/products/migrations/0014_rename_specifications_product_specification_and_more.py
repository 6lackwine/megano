# Generated by Django 4.2.5 on 2023-09-30 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_rename_reviews_product_review_alter_review_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='specifications',
            new_name='specification',
        ),
        migrations.AlterField(
            model_name='productspecification',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='products.product'),
        ),
    ]