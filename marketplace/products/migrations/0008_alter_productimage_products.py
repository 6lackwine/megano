# Generated by Django 4.2.5 on 2023-09-29 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_productspecification_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
