
from django.urls import path

from . import views

urlpatterns = [
    path("", views.loginView, name="login"),
    path("logout", views.logout, name="logout"),
    path("signup", views.signup, name="signup"),
    path("homepage", views.homepage, name="homepage"),
]