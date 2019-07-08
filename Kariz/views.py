from django.shortcuts import render
#from .serializers import userloginserialize
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission, AllowAny, IsAdminUser
from Kariz.models import Project , Employer
from .serializers import *
from .permissions import dashboardpermission
from rest_framework.response import Response
from rest_framework import status



class createproject(generics.CreateAPIView) :
    queryset = Project.objects
    serializer_class = projectcreationserializer
    #permission_classes = (AllowAny)


class signup(generics.CreateAPIView):
    queryset = User.objects
    serializer_class = userserialize
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        if instance:
            self.queryset = Employer.objects
            self.serializer_class = EmployerSerializer
            serializer2 = self.get_serializer(data=request.data)
            serializer2.is_valid(raise_exception=True)
            self.perform_create(serializer2)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()



class projectlisthandler(generics.ListAPIView):
    lookup_url_kwarg = 'category'
    serializer_class = projectlistserializer
    def get_queryset(self):
        _category = self.kwargs.get(self.lookup_url_kwarg)
        projects = Project.objects.filter(category=_category)
        return projects

class searchhandler(generics.ListAPIView):
    lookup_url_kwarg = 'name'
    serializer_class = projectlistserializer
    def get_queryset(self):
        _name = self.kwargs.get(self.lookup_url_kwarg)
        projects = Project.objects.filter(name=_name)
        return projects

class projectlhandler(generics.ListAPIView):
    lookup_url_kwarg = 'id'
    serializer_class = projectlistserializer
    def get_queryset(self):
        _category = self.kwargs.get(self.lookup_url_kwarg)
        projects = Project.objects.filter(id=_category)
        return projects



class dashboardhandler(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,dashboardpermission)
    serializer_class = userserialize


