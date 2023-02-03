from django.shortcuts import render
from django.contrib.auth.models import User

from .models import User
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
def home_page(request):
    accounts = User.objects.all()
    #context = {"Users": user}
    print(accounts[1].__dict__)
    return render(request = request, template_name = "login.html")


def get_users(request):
    accounts = User.objects.all()
    #context = {"Users": user}
    print(accounts.all)
    return render(request = request, template_name = "login.html")