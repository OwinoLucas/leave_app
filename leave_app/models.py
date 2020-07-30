# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70,blank=True, null=True)
    last_name = models.CharField(max_length=70,blank=True, null=True)
    id_number = models.IntegerField(blank=True)
    data_of_employment = models.DateTimeField( null=False, blank=False)
    gender = models.CharField(max_length=70,blank=True)
    department = models.CharField(max_length=70,blank=True)
    profile_pic = models.ImageField(upload_to='profile/',
                              blank=True)
    phone_number = models.CharField(max_length=70,blank=True)

    def __str__(self):
        return self.first_name

class Leave(models.Model):
    STATUSES = (
        ("approved","approved"),
        ("declined","declined"),
    )
    LEAVE_TYPE = (
        ("annual","annual"),
        ("sick","sick"),
        ("maternity","maternity"),
        ("paternity","paternity"),
        ("compassionate","compassionate"),
        ("study","study"),
        ("unpaid","unpaid"),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.TextField(max_length=10, choices = STATUSES)
    leave_app = models.TextField(max_length=20, choices = LEAVE_TYPE, null=True,blank=True)
    job_title = models.CharField(max_length=70,blank=True, null=True)
    date_applied = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)