from django.shortcuts import render
from laws . models import *
from level . models import *
from norms . models import *
from  . models import *
from django.contrib import auth
# для пошуку
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect

# для сумування обєктів
from django.db.models import Sum, Count, Avg, Max, Min

def start(request):
    return render(request, 'supervision.html', locals())


def home(request):
    username = auth.get_user(request).username
    if username:
        email = auth.get_user(request).email
        first_name = auth.get_user(request).first_name
        last_name = auth.get_user(request).last_name
    # context = {'username': username}
    obj = ArticleImage.objects.filter(is_active=True )
    objects_images = ArticleImage.objects.filter(is_active=True, is_main=True)
    print(objects_images)
    return render(request, 'base/home.html', locals())


def info(request):
    return render(request, 'base/info.html', locals())


def instruction(request):
    return render(request, 'base/instruction.html', locals())


def search(request):
    username = auth.get_user(request).username
    if username:
        email = auth.get_user(request).email
        first_name = auth.get_user(request).first_name
        last_name = auth.get_user(request).last_name
    if request.method == 'POST':
        request_value = request.POST['request_value']
        print (request_value)
        search_req = SearchRequest()
        search_req.request_value = request.POST.get("request_value")
        search_req.created = request.POST.get("created")
        search_req.updated = request.POST.get("updated")
        search_req.username = request.POST.get("username")
        search_req.save()

        print (request.POST)


        if request_value:
            model_1_result = Links.objects.filter (Q(normdock__name__icontains=request_value) |
                                             Q(normdock__pub_date__icontains=request_value) |
                                            Q(normdock__type__icontains=request_value) |
                                            Q(normdock__name_code__icontains=request_value))
            result1 = model_1_result.count()

            model_2_result = Description.objects.filter (Q(descr_name__icontains=request_value) |
                                            Q(law_title__icontains=request_value)|
                                            Q(objecttype__supervposition__full_name__icontains=request_value)|
                                            Q(objecttype__headline__icontains=request_value) |
                                            Q(objecttype__pub_date__icontains=request_value))

            result2 = model_2_result.count()
            total_results = result1 + result2


            if model_1_result:
                print("model_1_result")
            if model_2_result:
                print("model_2_result")
                print (total_results)

                return render(request,'base/search.html', locals())

        else:
            return HttpResponseRedirect('/search/', locals())

    return render(request, 'base/search.html', locals())
