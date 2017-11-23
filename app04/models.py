from django.db import models
from django.template.defaultfilters import default

# Create your models here.
class UserInfo(models.Model):
    username =  models.CharField(max_length=50)
    age = models.IntegerField()
class UserData(models.Model):
    username =  models.CharField(max_length=50)
    age = models.IntegerField()
class UserList(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
class SvnRev(models.Model):
    svnreversion = models.IntegerField()
    #svnreversion_old = models.IntegerField(default=0)
class svn_project(models.Model):
    project = models.CharField(max_length=100)
    svndir = models.CharField(max_length=100)
    new_svn_version = models.IntegerField()
    old_svn_version = models.IntegerField()
        
    
