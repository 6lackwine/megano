# Generated by Django 4.2.5 on 2023-11-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profiles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
