from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django import forms
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import User, Project, Media

#FORMS

#LOGIN
class formLogin(forms.Form):
    username = forms.CharField(label='title', max_length=64)
    password = forms.CharField(label='password', max_length=64)

#SIGN UP
class registrationForm(forms.Form):
    username = forms.CharField(label='title', max_length=64)
    password = forms.CharField(widget=forms.Textarea(attrs={'class': 'input'}))
    confirmation = forms.CharField(widget=forms.Textarea(attrs={'class': 'input'}))
    email= forms.CharField(widget=forms.Textarea(attrs={'class': 'input'}))


def homepage(request):  
    user = request.user
    projects = Project.objects.all()

    return render(request, "final/homepage.html", {        
        "user": user,
        "projects": projects
    })

def project(request, id):
    project = Project.objects.get(pk=id)
    media = Media.objects.filter(project=project)
    print(media)
    urls = []
    for url in media:
        urls.append(url.url)    
    print(urls)
    return render(request, "final/project.html", {        
        "project": project
    })

# AUTH
#LOGIN VIEW
def loginView(request):
    loginForm = formLogin()
    if request.method == "POST":
        form = formLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.get(username = username)
            #print(user.check_password(password)) Returning true as of now!
           
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
            else:
                return render(request, "final/login.html", {
                    "message": "Invalid username and/or password."
                })
    else:
        return render(request, "final/login.html",{
            "loginForm": loginForm
        })
    
# LOGOUT VIEW
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

# SIGNUP VIEW
def signup(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['confirmation']:
                return render(request, "final/signup.html", {
                    "registrationForm": registrationForm,
                    "message": "Passwords must match!"
                })
            else:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                email = form.cleaned_data['email']

                try:
                    user = User.objects.create_user(username, email)
                    user.set_password(password)
                    user.save()
                    return render(request, "final/login.html", {
                    
                    })
                except IntegrityError:
                    return render(request, "final/signup.html", {
                    "registrationForm": registrationForm,
                    "message": "Username already taken."
                })

    else:
            return render(request, "final/signup.html", {
                "registrationForm": registrationForm
            })
