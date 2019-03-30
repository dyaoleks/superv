from django import forms
import os
from django.conf import settings
from django.db import models
from django.core.files import File
from django.contrib.auth.models import User


class SearchRequest(models.Model):
    username = models.CharField(max_length=48, blank=True, null=True, default=None)
    request_value = models.CharField(max_length=128, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    total_results = models.CharField(max_length=8, blank=True, null=True, default=None)

    # for sorting by date of publ.
    class Meta:
        ordering = ['-created']

        verbose_name = "Пошуковий запит"
        verbose_name_plural = "Пошукові запити"

    def __str__(self):
        return "%s" % (self.id)
