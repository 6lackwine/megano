# Generated by Django 4.2.5 on 2023-11-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='products.tag', verbose_name='Тег'),
        ),
    ]
