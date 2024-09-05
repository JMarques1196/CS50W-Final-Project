from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# Projects that can be added or modified by an admin
class Project(models.Model):
    title = models.CharField(max_length=64)