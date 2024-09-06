from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# Projects that can be added or modified by an admin

class Project(models.Model):
    title = models.CharField(max_length=64)
    body = models.CharField(max_length = 500)

class Media(models.Model):
    project = models.ForeignKey(Project, max_length=150,  null=True, on_delete=models.CASCADE)
    url = models.CharField(max_length = 500)