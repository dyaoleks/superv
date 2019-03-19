from django import forms
import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class SupervChapter(models.Model):
    full_name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class SupervPosition(models.Model):
    full_name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class ObjectType(models.Model):
    id_num = models.CharField(max_length=8, blank=True, null=True, default=None)
    pub_date = models.DateField()
    headline = models.CharField(max_length=128)
    supervchapter = models.ForeignKey(SupervChapter, on_delete=models.CASCADE, blank=True, null=True, default=None)
    supervposition = models.ForeignKey(SupervPosition, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)


    # for sorting by date of publ.
    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return "%s" % (self.headline)


class Description(models.Model):
    objecttype = models.ForeignKey(ObjectType, on_delete=models.CASCADE, blank=True, null=True, default=None)
    descr_is_active = models.BooleanField(default=True)
    descr_name = models.TextField(max_length=2048, blank=True, null=True, default=None)
    law_title = models.CharField(max_length=1024, blank=True, null=True, default=None)
    law_chapter = models.CharField(max_length=128, blank=True, null=True, default=None)

    def __str__(self):
        return self.descr_name




class ArticleImage(models.Model):
    objecttype = models.ForeignKey(ObjectType, on_delete=models.CASCADE, blank=True, null=True, default=None)

    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def image_img(self):
        if self.image:
            return u' <img src="%s" width="100"/>' % self.image.url
        else:
            return u'(none)'
    image_img.short_description = 'Перегляд'
    image_img.allow_tags=True

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "%s" % (self.id)


