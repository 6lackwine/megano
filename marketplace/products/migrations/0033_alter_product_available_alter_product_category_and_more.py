# Generated by Django 4.2.5 on 2023-11-17 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_delete_catalog'),
        ('products', '0032_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Наличие'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.categories', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=100, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='freeDelivery',
            field=models.BooleanField(default=True, verbose_name='Бесплатная доставка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='fullDescription',
            field=models.TextField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productimage', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='limited',
            field=models.BooleanField(default=True, verbose_name='Лимитированный товар'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.review', verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productspecification', verbose_name='Характеристика'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='products.tag', verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название'),
        ),
    ]
