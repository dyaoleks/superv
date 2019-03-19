from django.contrib import admin
from . models import *


class IndexesInline(admin.TabularInline):
    model = Indexes
    extra = 0

class CriteriaAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Criteria._meta.fields ]
    inlines = [IndexesInline]

    class Meta:
        model = Criteria
admin.site.register(Criteria, CriteriaAdmin)

class IndexesAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Indexes._meta.fields]

    class Meta:
        model = Indexes
admin.site.register(Indexes, IndexesAdmin)






