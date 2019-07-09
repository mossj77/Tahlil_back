from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission, AllowAny, IsAdminUser
from Kariz.models import Project , Employer
from django.contrib.auth.models import User
from .serializers import *
from .permissions import dashboardpermission
from rest_framework.response import Response
from rest_framework import status



class createproject(generics.CreateAPIView):
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
            # for add employer account
            employer = Employer.objects.create(username=instance.username)
            employer.save()
            # for add free lancer account
            freelancer = FreeLancer.objects.create(username=instance.username)
            freelancer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


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
    permission_classes = (IsAuthenticated,)
    serializer_class = userserialize
    queryset = User
    lookup_field = 'username'
    def retrieve(self, request, *args, **kwargs):
        #self.lookup_field = request.user.username
        instance = self.get_object()
        userserializer = self.get_serializer(instance)
        self.serializer_class = FreeLancerSerializer
        self.queryset = FreeLancer
        instance = self.get_object()
        freelancerserializer = self.get_serializer(instance)
        self.serializer_class = EmployerSerializer
        self.queryset = Employer
        instance = self.get_object()
        employerserializer = self.get_serializer(instance)
        data = (userserializer.data,
                freelancerserializer.data,
                employerserializer.data)
        return Response(data)


'''
class teachingpermission(generics.RetrieveAPIView):
    lookup_url_kwarg = 'FreeLancerid'
    serializer_class = teachingpermissionserializer
    def get_queryset(self):
        _FreeLancerid = self.kwargs.get(self.lookup_url_kwarg)
        aFreeLancer = FreeLancer.objects.filter(FreeLancerid=_FreeLancerid)
        return aFreeLancer
'''
    #make a FreeLancer model that is : freelancer = USER+ {int score , boolean teachingform}



class requestforproject(generics.RetrieveAPIView):
    lookup_url_kwarg = 'name'
    serializer_class = projectlistserializer
    def get_queryset(self):
        _name = self.kwargs.get(self.lookup_url_kwarg)
        aproject = Project.objects.filter(name=_name)
        return aproject
