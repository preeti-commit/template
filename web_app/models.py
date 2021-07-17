# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    email= models.EmailField(max_length=255, blank=False)
    salary = models.CharField(max_length=255, blank=False)
    deduction = models.CharField(max_length=200, blank=False)
    gross_pay = models.CharField(max_length=200, blank=False)
