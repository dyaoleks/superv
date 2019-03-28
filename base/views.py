from django.shortcuts import render
from laws . models import *
from level . models import *
from norms . models import *
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
        print (username)

    else:
        print ('шо за нахуй')
    if request.method == 'POST':
        print (request.POST)
        srch = request.POST['srh']
        print (srch)

        if srch:
            model_1_result = Links.objects.filter (Q(normdock__name__icontains=srch) |
                                             Q(normdock__pub_date__icontains=srch) |
                                            Q(normdock__type__icontains=srch) |
                                            Q(normdock__name_code__icontains=srch))
            result1 = model_1_result.count()

            model_2_result = Description.objects.filter (Q(descr_name__icontains=srch) |
                                            Q(law_title__icontains=srch)|
                                            Q(objecttype__supervposition__full_name__icontains=srch)|
                                            Q(objecttype__pub_date__icontains=srch))
                                            # Q(supervchapter__icontains=srch)
            result2 = model_2_result.count()
            total_results = result1 + result2
            if model_1_result:
                print("model_1_result")
            if model_2_result:
                print("model_2_result")
                print (total_results)
                return render(request,'base/search.html', locals())

            # else:
            #     messages.error(request, 'Збігів не знайдено', locals())
            if model_2_result:
                print("model_2_result")
                return render(request,'base/search.html', locals())
            # else:
            #     messages.error(request, 'Збігів не знайдено', locals())
        else:
            return HttpResponseRedirect('/search/', locals())

    return render(request, 'base/search.html', locals())

