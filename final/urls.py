
from django.urls import path

from . import views

urlpatterns = [
    path("", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path("signup", views.signup, name="signup"),
    path("homepage", views.homepage, name="homepage"),
    path("project/<int:id>", views.project, name="project"),
    path("save", views.save, name="save"),
    path("check", views.check, name="check"),
]