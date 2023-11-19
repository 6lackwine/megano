from django.contrib import admin

from profiles.models import Profiles, ProfileAvatar


class ProfileAvatarInline(admin.TabularInline):
    model = ProfileAvatar

@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        ProfileAvatarInline,
    ]
    list_display = "pk", "user", "fullName", "email", "phone"
    fieldsets = [
        (None, {
            "fields": ("user", "fullName", "email", "phone")
        })
    ]
    search_fields = ["user", "fullName", "phone"]