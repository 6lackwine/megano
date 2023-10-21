import json

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView

from profiles.models import Profiles
from profiles.serializers import ProfileSerializers, UserSerializers


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

class SignUpAPIView(APIView):
    def post(self, request):
        user_data = json.loads(request.body)
        name = user_data["name"]
        username = user_data["username"]
        password = user_data["password"]
        User.objects.create(username=username,
                            first_name=name,
                            password=password
                            )
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=200)
        else:
            return Response()

@api_view(["POST"])
def sign_out(request):
    logout(request)
    return reverse_lazy('profiles:login')

@api_view(["POST"])
def sign_in(request):
    if request.method == "POST":
        user_data = json.loads(request.body)
        username = user_data["username"]
        password = user_data["password"]
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            return Response(status=200)

    # if request.method == "POST":
    #     json_string = request.body.decode('utf-8')
    #     data_dict = json.loads(json_string)
    #     username = data_dict['username']
    #     password = data_dict['password']
    #     if username and password:
    #         user = authenticate(request, username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return HttpResponse(status=200)
