from rest_framework import serializers

from profiles.models import Profiles, ProfileAvatar


class ProfileAvatarSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileAvatar
        fields = "src", "alt"

class ProfileSerializers(serializers.ModelSerializer):
    avatar = ProfileAvatarSerializers()
    class Meta:
        model = Profiles
        fields = "fullName", "email", "phone", "avatar"