# Generated by Django 4.2.5 on 2023-10-01 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_user'),
        ('profiles', '0002_remove_profile_user_profiles_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]