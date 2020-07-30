# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime as dt

# Create your models here.
class Employee(models.Model):
    SEX_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',)
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.IntegerField(blank=True,null=True)
    date_of_employment = models.DateField( null=True, blank=False)
    gender = models.CharField(max_length=7,choices=SEX_CHOICES)
    department = models.CharField(max_length=70,blank=True)
    profile_pic = models.ImageField(upload_to='profile/',
                              blank=True)
    phone_number = models.CharField(max_length=70,blank=True)

    def __str__(self):
        return self.user.username


    @property
    def profile_pic_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/media/default.png"

    def save_employee(self):
        self.save()

    def update_employee(self, using=None, fields=None, **kwargs):
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_employee(self):
        self.delete()

    def create_employee_profile(sender, **kwargs):
        if kwargs['created']:
            employee_profile = Employee.objects.create(user=kwargs['instance'])
        
    post_save.connect(create_employee_profile, sender=User)


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