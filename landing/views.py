# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
# from django.shortcuts import render
from django.contrib import auth
from django.template.context_processors import csrf

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect



def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        print(user)
        print(username)
        print(request.POST)
        if user is not None:
            # username = auth.get_user(request).username
            auth.login(request, user)
            return HttpResponseRedirect('/home/')
        else:
            login_error = "Не вірний логін або пароль"
            context={"login_error":login_error}
            print({"login_error":login_error})
            return render(request,'landing/index.html', context)
    else:
        return render(request, 'landing/index.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/home/')


