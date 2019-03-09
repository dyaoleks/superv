from django.shortcuts import render

from . models import *
from django.contrib import auth

def start(request):
    return render(request, 'supervision.html', locals())


def home(request):
    username = auth.get_user(request).username
    context = {'username': username}
    return render(request, 'base.html', locals())