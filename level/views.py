from django.shortcuts import render
from . models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound
from django.template import RequestContext
from django.contrib import auth
from django.shortcuts import render_to_response

# для сумування обєктів
from django.db.models import Sum

# получение данных из бд
def level(request):
    level = Criteria.objects.all()
    username = auth.get_user(request).username
    if username:
        email = auth.get_user(request).email
        first_name = auth.get_user(request).first_name
    total_level = Criteria.objects.filter(is_main=True).aggregate(Sum ('scores'))
    return render(request, "level/level.html", locals())

# {"level": level, "total_level": total_level},


# сохранение данных в бд
def create(request):
    username = auth.get_user(request).username
    email = auth.get_user(request).email
    if request.method == "POST":
        level = Criteria()
        level.name = request.POST.get("name")
        level.index_name = request.POST.get("index_name")
        level.scores = request.POST.get("scores")
        level.username = request.POST.get("username")
        level.is_main = request.POST.get("is_main")
        level.save()

    return HttpResponseRedirect("/level/", locals())


# изменение данных в бд
def edit(request, id):
    username = auth.get_user(request).username
    try:
        level = Criteria.objects.get(id=id)

        if request.method == "POST":
            print (request.POST)
            # level.name = request.POST.get("name")
            # level.index_name = request.POST.get("index_name")
            # level.scores = request.POST.get("scores")
            level.is_main = request.POST.get("is_main")
            level.username = request.POST.get("username")
            level.save()

            return HttpResponseRedirect("/level/#risk")
        else:
            return render(request, "level/edit.html", locals()) #{"level": level}
    except Criteria.DoesNotExist:
        return HttpResponseNotFound("<h2>Критерій не знайдено</h2>")


# удаление данных из бд
def delete(request, id):
    username = auth.get_user(request).username
    try:
        level = Criteria.objects.get(id=id)
        level.delete()
        return HttpResponseRedirect("/level/",locals())
    except Criteria.DoesNotExist:
        return HttpResponseNotFound("<h2>Критерій не знайдено</h2>")


def high(request):
    username = auth.get_user(request).username
    return render(request, "level/high.html", locals())


def middle(request):
    username = auth.get_user(request).username
    return render(request, "level/middle.html", locals())


def low(request):
    username = auth.get_user(request).username
    return render(request, "level/low.html", locals())


