# Generated by Django 4.2.5 on 2023-09-29 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_productimage_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='images',
        ),
    ]
