# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime as dt
from dateutil.relativedelta import relativedelta

# Create your models here.
class Employee(models.Model):
    SEX_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )
    STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Entanglement', 'Entanglement')
    )
    GROUP = (
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('O-', 'O-')
    )
    DEPT = (
        ('Operations', 'Operations'),
        ('Marketing & Sales', 'Marketing & Sales'),
        ('Programs', 'Programs'),
        ('Editorial', 'Editorial'),
        ('Technical', 'Technical'),
        ('Digital', 'Digital'),
        ('Graphics', 'Graphics'),
        ('Innovations', 'Innovations'),
        ('Bureau Heads', 'Bureau Heads'),
        ('C.E.O', 'C.E.O')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.IntegerField(blank=True,null=True)
    date_of_employment = models.DateField( null=True, blank=False)
    gender = models.CharField(max_length=7,choices=SEX_CHOICES)
    department = models.CharField(max_length=70,choices=DEPT,null=True)
    profile_pic = models.ImageField(upload_to='profile/',
                              blank=True)
    phone_number = models.CharField(max_length=70,blank=True)
    blood_group = models.CharField(max_length=7,choices=GROUP,null=True)
    marital_status = models.CharField(max_length=15,choices=STATUS,null=True)
    address = models.CharField(max_length=70,blank=True)
    job_title = models.CharField(max_length=70,blank=True, null=True)

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

    

class Next_of_kin(models.Model):
    kin = models.ForeignKey(Employee, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20, blank=True)
    dials = models.CharField(max_length=70,blank=True)
    email = models.EmailField(max_length=70, blank=True)
    address = models.CharField(max_length=70,blank=True)
    relation = models.CharField(max_length=70,blank=True)

class Leave(models.Model):
    STATUSES = (
        ("Approved","Approved"),
        ("Declined","Declined"),
        ("Pending","Pending"),
    )
    LEAVE_TYPE = (
        ("Annual","Annual"),
        ("Sick","Sick"),
        ("Maternity","Maternity"),
        ("Paternity","Paternity"),
        ("Compassionate","Compassionate"),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.TextField(max_length=10, choices = STATUSES, default='Pending')
    leave_app = models.TextField(max_length=20, choices = LEAVE_TYPE, null=True,blank=True)
    date_applied = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)

    def save_leave(self):
        self.save()

    def update_leave(self, using=None, fields=None, **kwargs):
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_leave(self):
        self.delete()

    @property
    def working_days_in_leave_period(self):
        date_counter = self.start_date
        weekdays_counter = 0
        while date_counter <= self.end_date:
            #0 is monday, 6 is sunday
            if date_counter.weekday() < 5:
                weekdays_counter += 1
            date_counter += relativedelta(days=1)
        return weekdays_counter

    def leave_qualification(self):
        day_one = Employee.date_of_employment
        
        if date.today() - day_one <= 365:
            return 'You have to serve an year or more to qualify'
        else:
            return 'You are qualified'

    # @property
    # def annual_leave_calc(self):
    #     monthly_leave_days = 1.75
    #     months = 12
