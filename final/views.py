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
from .models import User, Project, Media, Message, CheckList

#FORMS

#LOGIN
class formLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), label=False, max_length=64)
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}), label=False, max_length=64)

#SIGN UP
class registrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),label=False, max_length=64)
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}),label=False)
    confirmation = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirmation'}),label=False)
    email= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}),label=False)

#MESSAGE 
class messageForm(forms.Form):
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add a new comment'}), max_length='150', label=False)

# VIEWS
def homepage(request):  
    user = request.user
    projects = Project.objects.all()

    return render(request, "final/homepage.html", {        
        "user": user,
        "projects": projects
    })

def project(request, id, *args, **kwargs):
    # Get both the projects and its corresponding urls
    project = Project.objects.get(pk=id)
    resources = Media.objects.filter(project=project)
    savedComments = Message.objects.filter(project = project)
    listItems = CheckList.objects.filter(project=project)
    # Add a form for the messages

    return render(request, "final/project.html" ,{        
        "project": project,
        "resources": resources,
        "savedComments": savedComments,
        "listItems": listItems,
    })

# View for saving chat comments, so we can have a chat history
@csrf_exempt
def save(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            project = Project.objects.get(pk = data['id'])
            newMessage = Message(author = request.user, project=project, content = data['message'])
            newMessage.save()
 
            return JsonResponse({}, status=200)
        except:
            return JsonResponse({}, status=400)
        
@csrf_exempt
def check(request):
    if request.method == "POST":
        try:
            checkbox = json.loads(request.body)
            checkList = CheckList.objects.get(pk = checkbox['id'])
            if checkList.status == True:
                checkList.status = False
            else:
                checkList.status = True
            
            checkList.save()
     
            return JsonResponse({
            }, status=200)
        except:
            return JsonResponse({}, status=400)

# AUTH
#LOGIN VIEW
def loginView(request):
    loginForm = formLogin()
    if request.method == "POST":
        form = formLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
            else:
                return render(request, "final/login.html", {
                    "message": "Invalid username and/or password.",
                    "loginForm": loginForm
                })
    else:
        """ Make the login page unavailable when a user is loged in """
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("homepage"))
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
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "final/signup.html", {
                "registrationForm": registrationForm
            })



