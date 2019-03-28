from django import forms
import os
from django.conf import settings
from django.db import models


class Criteria(models.Model):
    username = models.CharField(max_length=500, blank=True, null=True, default=None)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    name = models.CharField(max_length=500, blank=True, null=True, default=None)
    index_name = models.CharField(max_length=500)
    scores = models.IntegerField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False, blank=True, null=True,)




    # for sorting by date of publ.
    class Meta:
        ordering = ['id']

        verbose_name = "Критерій"
        verbose_name_plural = "Критерії"

        def __str__(self):
            return "%s" % (self.id)
