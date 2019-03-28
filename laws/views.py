from django.shortcuts import render
from django.db.models import Q
from . models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib import auth


def object(request, object_id):
    object = ObjectType.objects.get(id=object_id)
    username = auth.get_user(request).username

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)
    return render(request,'laws/laws.html',locals())









