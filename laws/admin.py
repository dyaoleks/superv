from django.contrib import admin
from . models import *


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 0

class DescriptionInline(admin.TabularInline):
    model = Description
    extra = 0


class ObjectTypeAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ObjectType._meta.fields ]
    inlines = [ArticleImageInline, DescriptionInline]

    class Meta:
        model = ObjectType
admin.site.register(ObjectType, ObjectTypeAdmin)

class DescriptionAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Description._meta.fields ]

    class Meta:
        model = Description
admin.site.register(Description, DescriptionAdmin)

class SupervChapterAdmin (admin.ModelAdmin):
    list_display = [field.name for field in SupervChapter._meta.fields]

    class Meta:
        model = SupervChapter
admin.site.register(SupervChapter, SupervChapterAdmin)


class SupervPositionAdmin (admin.ModelAdmin):
    list_display = [field.name for field in SupervPosition._meta.fields]

    class Meta:
        model = SupervPosition
admin.site.register(SupervPosition, SupervPositionAdmin)














class ArticleImageAdmin (admin.ModelAdmin):
    list_display = ['id', 'image_img','created']

    class Meta:
        model = ArticleImage
admin.site.register(ArticleImage, ArticleImageAdmin)