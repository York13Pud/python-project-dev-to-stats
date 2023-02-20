from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from .modules.dev_to_api_articles import get_published_articles
from .modules.dev_to_process_data import testing_function

import environ

# --- Create your views here.

def show_stats(request):
    return redirect(to = "home")


@login_required(login_url = "login")
def process_published_articles(request):
    env = environ.Env(DEBUG=(bool, False))
    
    dev_to_api_key = env("DEV_TO_API_KEY")
    api_endpoint_url = "https://dev.to/api/articles/me/published"
    
    published_articles = get_published_articles(api_key = dev_to_api_key,
                                                api_endpoint = api_endpoint_url)
    
    # print("hello")
    print(published_articles)
    
    return redirect(to = "home")


@login_required(login_url = "login")
def testing(request):
    data = testing_function()

    return redirect(to = "home")
    