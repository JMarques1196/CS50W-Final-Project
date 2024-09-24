from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# Projects that can be added or modified by an admin

class Project(models.Model):
    title = models.CharField(max_length=64)
    body = models.CharField(max_length = 500)
    coverImage = models.CharField(max_length = 500)
    link = models.CharField(max_length=200)

class Media(models.Model):
    project = models.ForeignKey(Project, max_length=150,  null=True, on_delete=models.CASCADE)
    url = models.CharField(max_length = 500)
    resourceTitle = models.CharField(max_length = 150)
    resource = models.CharField(max_length = 500)

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="author")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name="project")
    content = models.CharField(max_length=150)

class CheckList(models.Model):
    project = models.ForeignKey(Project, max_length=150, null=True, on_delete=models.CASCADE)
    item = models.CharField(max_length=150)
    status = models.BooleanField(default=False)