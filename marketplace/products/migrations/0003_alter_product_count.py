# Generated by Django 4.2.5 on 2023-11-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
    ]
