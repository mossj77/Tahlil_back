from rest_framework import serializers
from rest_framework.serializers import CharField,HyperlinkedIdentityField,ModelSerializer,SerializerMethodField,ValidationError
from django.contrib.auth.models import User
from .models import  Project , Employer
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q


class userserialize(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'last_name', 'first_name', 'email')

class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = ('username', 'password')

class projectcreationserializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class loginserializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    userName = CharField(allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = ('userName', 'password')
        extra_kwargs = {"password":
                            {"write_only":True}
                        }
    def validate(self, data):
        user_obj = None
        userName = data.get("userName",None)
        password = data["password"]
        if not userName:
            raise ValidationError("A username is required to login")
        user = User.objects.filter(
            Q(userName=userName)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:raise ValidationError("This username is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("")

        data["token"] = "random token"
        return data


class projectlistserializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
