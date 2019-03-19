from django import forms
import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Criteria(models.Model):
    pub_date = models.DateField()

    name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    sum = models.IntegerField(default=0)

    # for sorting by date of publ.
    class Meta:
        ordering = ['pub_date']

        verbose_name = "Критерій"
        verbose_name_plural = "Критерії"

    def __str__(self):
        return "%s" % (self.name)

    def save(self, *args, **kwards):
        super(Criteria, self).save(*args, **kwards)

#
class Indexes (models.Model):
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE, blank=True, null=True, default=None)
    index_name = models.CharField(max_length=500)
    scores = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    # for sorting by date of publ.
    class Meta:
        ordering = ['-index_name']

        verbose_name = "Показник "
        verbose_name_plural = "Показники"

    def __str__(self):
        return "%s" % (self.index_name)



    def save(self, *args, **kwargs):
        # scores = self.scores
        # self.scores = scores
        # criteria = self.criteria
        # all_criterias_inchoice = Criteria.objects.filter(criteria=criteria, is_active=True) # обираю усі активні значення критеріїв
        # sum = 0
        # for item in all_criterias_inchoice:
        #     sum+=item.scores
        # self.criteria.save(force_update=True)
        super(Indexes, self).save(*args, **kwargs)


