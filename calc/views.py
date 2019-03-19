from django.shortcuts import render
from django.db.models import Q
from . models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib import auth


def calc(request):
    return render(request,'calc/laws.html',locals())

