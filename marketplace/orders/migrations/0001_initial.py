# Generated by Django 4.2.5 on 2023-09-16 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100)),
                ('deliveryType', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('paymentType', models.CharField(max_length=100)),
                ('totalCost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('products', models.ManyToManyField(related_name='orders', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='profiles.profile')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['pk', 'createdAt', 'status'],
            },
        ),
    ]