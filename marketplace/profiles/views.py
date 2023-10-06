from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import RetrieveUpdateAPIView

from profiles.models import Profiles
from profiles.serializers import ProfileSerializers


# class ProfileAPIView(APIView):
#     def get(self, request: Request):
#         profile = Profiles.objects.get(user=request.user)
#         serialized = ProfileSerializers(profile)
#         return Response(serialized.data)

class ProfileAPIView(RetrieveUpdateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfileSerializers

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.pk)
        self.check_object_permissions(self.request, obj)
        return obj