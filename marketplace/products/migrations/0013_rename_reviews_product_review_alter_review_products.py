# Generated by Django 4.2.5 on 2023-09-30 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_rename_tags_product_tag_alter_tag_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='reviews',
            new_name='review',
        ),
        migrations.AlterField(
            model_name='review',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='products.product'),
        ),
    ]
