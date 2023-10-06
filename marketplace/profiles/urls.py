from django.urls import path

from profiles.views import ProfileAPIView

urlpatterns = [
    path("profile/", ProfileAPIView.as_view(), name="my_profile"),
]