from django.shortcuts import render
from laws . models import *
from django.contrib import auth


def start(request):
    return render(request, 'supervision.html', locals())

def home(request):
    username = auth.get_user(request).username
    context = {'username': username}
    obj = ArticleImage.objects.filter(is_active=True )
    objects_images = ArticleImage.objects.filter(is_active=True, is_main=True)
    print(objects_images)
    return render(request, 'base/home.html', locals())

def info(request):
    return render(request, 'base/info.html', locals())

def instruction(request):
    return render(request, 'base/instruction.html', locals())