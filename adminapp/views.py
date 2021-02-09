from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import UsersLoginForm, UsersRegistration, UsersProfileForm
from django.contrib import auth
from django.urls import reverse
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'adminapp/admin.html')

def users_create(request):
    return render(request, 'adminapp/admin-users-create.html')


def users_read(request):
    return render(request, 'adminapp/admin-users-read.html')


def users_update(request):
    return render(request, 'adminapp/admin-users-update-delete.html')

def users_delete(request):
    pass