from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    class Meta:
        ordering = ["pk",]
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="users")
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)

def profile_avatar_path(instance: "ProfileAvatar", filename: str) -> str:
    return "profile/profile_{pk}/users/{filemane}".format(
        pk=instance.profile.pk,
        filename=filename,
    )

class ProfileAvatar(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    image = models.FileField(upload_to=profile_avatar_path)