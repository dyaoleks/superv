from django.contrib import admin
from . models import *

class SearchRequestAdmin (admin.ModelAdmin):
    list_display = [field.name for field in SearchRequest._meta.fields ]

    class Meta:
        model = SearchRequest
admin.site.register(SearchRequest, SearchRequestAdmin)
