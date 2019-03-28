from django.conf.urls import url
from . import views
from django.http import HttpResponseNotFound

urlpatterns = [

    url(r'^level/$', views.level, name='level'),
    url(r'^level/create/$', views.create, name='create'),
    url(r'^level/edit/(?P<id>\w+)/$', views.edit, name='edit'),
    url(r'^level/delete/(?P<id>\w+)/$', views.delete, name='delete'),
    url(r'^level/high/$', views.high, name='high'),
    url(r'^level/middle/$', views.middle, name='middle'),
    url(r'^level/low/$', views.low, name='low'),
]