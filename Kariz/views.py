from django.shortcuts import render
#from .serializers import userloginserialize
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission, AllowAny, IsAdminUser
from Kariz.models import Project
from .serializers import *
from .permissions import dashboardpermission



class createproject(generics.CreateAPIView) :
    queryset = Project.objects
    serializer_class = projectcreationserializer
    #permission_classes = (AllowAny)


class signup(generics.CreateAPIView):
    queryset = User.objects
    serializer_class = userserialize


class teachinginfo(generics.CreateAPIView):
    queryset = teachingform.objects
    serializer_class = teachingformserializer


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


'''
class teachingpermission(generics.RetrieveAPIView):
    lookup_url_kwarg = 'FreeLancerid'
    serializer_class = teachingpermissionserializer
    def get_queryset(self):
        _FreeLancerid = self.kwargs.get(self.lookup_url_kwarg)
        aFreeLancer = FreeLancer.objects.filter(FreeLancerid=_FreeLancerid)
        return aFreeLancer
'''
    #make a FreeLancer model that is : freelancer = USER+ {int score , etc}



class requestforproject(generics.RetrieveAPIView):
    lookup_url_kwarg = 'projectname'
    serializer_class = projectlistserializer
    def get_queryset(self):
        _projectname = self.kwargs.get(self.lookup_url_kwarg)
        aproject = Project.objects.filter(projectname=_projectname)
        return aproject
