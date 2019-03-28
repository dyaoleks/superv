from django.contrib import admin
from . models import *

class CriteriaAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Criteria._meta.fields ]

    class Meta:
        model = Criteria
admin.site.register(Criteria, CriteriaAdmin)

