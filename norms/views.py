from django.shortcuts import render
from django.db.models import Q
from . models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render_to_response
from django.template import RequestContext

def norm(request):
    username = auth.get_user(request).username
    context = {'username': username}
    links = Links.objects.filter(is_active=True, normdock__is_active=True)
    last_added_docks=links.filter(is_active=True).order_by('-id')[:2] # Показує лише останні додані документи. У дужках визначається кількість
    docs_dbn = links.filter(normdock__category__id=1) # Розподіляється за типом (категорією) документу по групам
    docs_snip = links.filter(normdock__category__id=2)
    return render(request,'norms/norm.html',locals())


def rules (request):
    username = auth.get_user(request).username
    context = {'username': username}
    links = Links.objects.filter(is_active=True, normdock__is_active=True)
    last_added_docks=links.filter(is_active=True).order_by('-id')[:2] # Показує лише останні додані документи. У дужках визначається кількість
    docs_rules = links.filter(normdock__category__id=3)
    return render(request,'norms/rules.html',locals())


def guid (request):
    username = auth.get_user(request).username
    context = {'username': username}
    links = Links.objects.filter(is_active=True, normdock__is_active=True)
    last_added_docks=links.filter(is_active=True).order_by('-id')[:2] # Показує лише останні додані документи. У дужках визначається кількість
    docs_dbn = links.filter(normdock__category__id=1) # Розподіляється за типом (категорією) документу по групам
    docs_snip = links.filter(normdock__category__id=2)
    docs_rules = links.filter(normdock__category__id=3)
    return render(request,'norms/guid.html',locals())