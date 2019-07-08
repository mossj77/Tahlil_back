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
    creatoruname = models.ForeignKey(User,on_delete=models.CASCADE ,null=True,blank=True)

    def __str__(self):
        return self.name

class teachingform(models.Model):
    category = models.CharField(max_length=150)
    ability = models.CharField(max_length=500)
    resume = models.CharField(max_length=2000)
