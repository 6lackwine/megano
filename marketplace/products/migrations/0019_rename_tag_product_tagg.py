# Generated by Django 4.2.5 on 2023-09-30 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_product_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tag',
            new_name='tagg',
        ),
    ]
