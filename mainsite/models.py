from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
     user = models.OneToOneField(User)
     bio = models.CharField(max_length=500)
     # papers =
     # photo =
     studentStatus = models.CharField(max_length=15)
     extension = models.IntegerField()
     labAff = models.CharField(max_length=50)

class Location(models.Model):
    room = models.CharField(max_length=10)

class Study(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location)
    paid = models.BooleanField()
    volunteer = models.BooleanField()
    experimetrix = models.BooleanField()
    maxPart = models.IntegerField()
    curPart = models.IntegerField()
    length = models.IntegerField()

class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(unique=True)