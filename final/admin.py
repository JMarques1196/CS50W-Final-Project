from django.contrib import admin
from .models import User, Project, Media, Message, CheckList
# Register your models here.
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Media)
admin.site.register(Message)
admin.site.register(CheckList)