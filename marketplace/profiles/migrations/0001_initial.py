# Generated by Django 4.2.5 on 2023-09-25 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ProfileAvatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=profiles.models.profile_avatar_path)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
