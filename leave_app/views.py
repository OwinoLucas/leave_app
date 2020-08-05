# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .decorators import unauthenticated_user
from .forms import *
from .models import *
import datetime

# Create your views here.
@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, username + ' ' + 'your account was created successfully!')
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in as' + ' ' + username)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username and/or Password')

    context = {}
    return render(request, 'auth/login.html', context)


def logoutUser(request):
    logout(request)
    messages.success(
        request, 'You have logged out. Log back in to access our services.')
    return redirect('login')

def home(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        e_form = EmployeeUpdateForm(
            request.POST, request.FILES, instance=request.user.employee)
        if u_form.is_valid() and e_form.is_valid():
            u_form.save()
            e_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        e_form = EmployeeUpdateForm(instance=request.user.employee)

    context = {'u_form': u_form,
               'e_form': e_form, }
    return render(request, 'profile.html', context)

def security(request):
    
    context = {}
    return render(request, 'security.html', context)

def notifications(request):
    
    context = {}
    return render(request, 'notifications.html', context)
