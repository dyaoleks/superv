from django.contrib import admin
from . models import *


class LinksInline(admin.TabularInline):
    model = Links
    extra = 0


class NormDockAdmin (admin.ModelAdmin):
    list_display = [field.name for field in NormDock._meta.fields ]
    inlines = [ LinksInline]

    class Meta:
        model = NormDock
admin.site.register(NormDock, NormDockAdmin)


class LinksAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Links._meta.fields ]

    class Meta:
        model = Links
admin.site.register(Links, LinksAdmin)

class CategoryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields ]

    class Meta:
        model = Category
admin.site.register(Category, CategoryAdmin)