from django.db import models
from django.contrib.auth.models import User



class Project(models.Model):
    category = models.CharField(max_length=150)
    name = models.CharField(max_length=200)
    skills = models.CharField(max_length=1000,blank=True)
    projectexplained = models.CharField(max_length=2000,blank=True)
    cost = models.IntegerField()
    fori = models.BooleanField()
    motamayez = models.BooleanField()
    creatoruname = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name




class Employer(models.Model):
    username = models.CharField(max_length=200,name='username', unique=True)
    Projects = models.ManyToManyField(Project, name='projects', null=True, blank=True)
    phone = models.CharField(max_length=12, name='phone', null=True, blank=True)
    def __str__(self):
        return self.username

class FreeLancer(models.Model):
    username = models.CharField(max_length=200, unique=True, name='username')
    CurrentProjects = models.ManyToManyField(Project, name='currentProjects', null=True, blank=True)
    numberOfAllProjects = models.IntegerField(default=0, name='numberOfAllProjects')
    numberOfDoneProjects = models.IntegerField(default=0, name='numberOfDoneProjects')
    score = models.IntegerField(default=0, name='sore')
    teachingpermission = models.BooleanField(default=False, name='teachingpermission')
    def __str__(self):
        return self.username

# class Company(models.Model):
#     username = models.CharField(max_length=200, unique=True, name='username')
#     address = models.CharField(max_length=1000, blank=True)
#     description = models.CharField(max_length=1000, blank=True)
#     skill = models.CharField(max_length=1000, blank=True)
#     phone = models.IntegerField(default=0, name='numberOfAllProjects')
#     score = models.IntegerField(default=0, name='sore')
#     CurrentProjects = models.ManyToManyField(Project, name='currentProjects', null=True, blank=True)
#     numberOfAllProjects = models.IntegerField(default=0, name='numberOfAllProjects')
#     numberOfDoneProjects = models.IntegerField(default=0, name='numberOfDoneProjects')



class teachingform(models.Model):
    category = models.CharField(max_length=150, blank=True)
    ability = models.CharField(max_length=500, blank=True)
    resume = models.CharField(max_length=2000, blank=True)
    username = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.username

