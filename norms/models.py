from django import forms
import os
from django.conf import settings
from django.db import models
from django.core.files import File
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=24)
    is_active = models.BooleanField(default=True)


    # for sorting by date of publ.
    class Meta:
        ordering = ['name']

        verbose_name = "Тип документу"
        verbose_name_plural = "Типи документів"

    def __str__(self):
        return "%s" % (self.name)

class NormDock(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, default=None)
    pub_date = models.DateField()
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=12, blank=True, null=True, default=None  )
    name_code = models.CharField(max_length=24)
    is_active = models.BooleanField(default=True)


    # for sorting by date of publ.
    class Meta:
        ordering = ['-pub_date']

        verbose_name = "Нормативний документ"
        verbose_name_plural = "Нормативні документи"

    def __str__(self):
        return "%s" % (self.name_code)

class Links(models.Model):
    normdock = models.ForeignKey(NormDock, on_delete=models.CASCADE, blank=True, null=True, default=None)
    link_name = models.CharField(max_length=256, blank=True, null=True, default=None)
    file = models.FileField(upload_to='norm_files/', blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # for sorting by date of publ.
    class Meta:
        ordering = ['-created']

        verbose_name = "Посилання на документ"
        verbose_name_plural = "Посилання на документи"

    def __str__(self):
        return "%s" % (self.id)




