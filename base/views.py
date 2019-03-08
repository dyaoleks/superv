from django.shortcuts import render

from . models import *
from django.contrib import auth

def home(request):
    return render(request, 'Supervision.html', locals())