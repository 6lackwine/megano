# Generated by Django 4.2.5 on 2023-09-29 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_specification_product_specifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='review', to='products.product'),
        ),
    ]