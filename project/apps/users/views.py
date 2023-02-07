from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import User
from .forms import CreateUserForm
from .modules.dev_to_api import get_user_details

import json
import logging

# --- Settings for the logging configuration:
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'console': {
            'format': '%(levelname)s:%(asctime)s:%(name)s:%(message)s'
        },
        'file': {
            'format': '%(levelname)s:%(asctime)s:%(name)s:%(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': './apps/users/logs/debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': True,
        }
    }
})


logger = logging.getLogger(__name__)

# Create your views here.

@login_required(login_url = "login")
def home_page(request):
    return render(request = request, template_name = "home.html")


def login_user(request):
    # --- This will redirect a logged in user to profiles if they try
    # --- to access the login page directly.
    if request.user.is_authenticated:
        return redirect(to = "home")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request = request,
                           message = "Username does not exist")
        
        user = authenticate(request = request,
                            username = username,
                            password = password)
        
        if user is not None:
            login(request, user = user)
            return redirect("home")
        else:
            print("Username or password is incorrect")
    
    return render(request = request, template_name = "login.html")


@login_required(login_url = "login")
def logout_user(request):
    logout(request = request)
    return redirect(to = "login")


def register_api(request):

    if request.method == "POST":
        api_key = request.POST["api-key"]
        user_details = get_user_details(api_key = api_key)
        
        request.session["user_api_details"] = {
            "account_id": user_details["id"],
            "username": user_details["username"],
            "first_name": user_details["username"],
            "user_summary": user_details["summary"],
            "location": user_details["location"],
            "twitter_username": user_details["twitter_username"],
            "github_username": user_details["github_username"],
            "website_url": user_details["website_url"],
            "profile_image": user_details["profile_image"],
            "api_key": api_key,
            "joined_on": user_details["joined_at"],
        }
              
        return redirect(to = "register_details")
    
    return render(request = request, template_name = "register.html")


def register_details(request):
    context = request.session["user_api_details"]
    print(context)
    
    form = CreateUserForm(initial = context)
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        # --- The below will check if the form is valid. If so, it will
        # --- save tbe form data temporarily, set the username to lowercase,
        # --- save the user in the database, create a profile (signal),
        # --- return a success message and log the user in.
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            
            print("checkpoint 1")
            messages.success(request = request, 
                             message = "User account created!")

            print("checkpoint 2")
            login(request = request, user = user)
            return redirect(to = "home")
        
        # --- If the form is not valid, the user will get an error message.
        else:
            print("checkpoint 3")
            messages.error(request = request, 
                           message = "An error ocurred during registration. Please try again.")
    context["form"] = form
    print(context)
    print("checkpoint 4")
    return render(request = request, template_name = "register.html", context = context)


def user_account(request):
    return render(request = request, template_name = "login.html")