# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from web_app import models


class WorldAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Employee
admin.site.register(models.Employee, WorldAdmin)