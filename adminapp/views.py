from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from authapp.models import Users
from adminapp.forms import UserAdminRegistration, UserAdminUpdate
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda user: user.is_active)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda user: user.is_active)
def users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistration(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:read'))
    else:
        form = UserAdminRegistration()
    content = {
        'form': form
    }
    return render(request, 'adminapp/admin-users-create.html', content)


@user_passes_test(lambda user: user.is_active)
def users_read(request):
    content = {
        'users': Users.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', content)


@user_passes_test(lambda user: user.is_active)
def users_update(request, id):
    user = Users.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminUpdate(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:read'))
    else:
        form = UserAdminUpdate(instance=user)

    content = {
        'form': form,
        'current_user': user
    }
    return render(request, 'adminapp/admin-users-update-delete.html', content)


@user_passes_test(lambda user: user.is_active)
def users_delete(request, id):
    user = Users.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('adminapp:read'))
