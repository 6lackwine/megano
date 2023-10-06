from django.contrib.auth.models import User
from django.db import models

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="users")
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    image = models.ForeignKey("ProfileAvatar", on_delete=models.CASCADE)

def profile_avatar_path(instance: "ProfileAvatar", filename: str) -> str:
    return "profile/profile_{pk}/users/{filemane}".format(
        pk=instance.profile.pk,
        filename=filename,
    )

class ProfileAvatar(models.Model):
    profile = models.OneToOneField(Profiles, on_delete=models.CASCADE, related_name="avatar")
    src = models.FileField(upload_to=profile_avatar_path)
    alt = models.CharField(max_length=100)