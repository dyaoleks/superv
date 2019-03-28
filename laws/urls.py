from django.conf.urls import url
from laws import views

urlpatterns = [
    # url(r'^home/laws/$', views.laws, name='laws'),
    url(r'^object/(?P<object_id>\w+)/$', views.object, name='object'),
    # url(r'^search_laws/$', views.search_laws, name='search_laws'),

    # url(r'^landing123/', views.landing, name='landing'),
    # url(r'^news/', views.news, name='news'),
    # url(r'^articles/([0-9]{4})/$', views.year_archive),
    # url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    # url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]