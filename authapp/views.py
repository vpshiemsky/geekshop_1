from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserloginForm, ShopUserRegisterForm, ShopUserEditForm


def login(request):
    login_form = ShopUserloginForm(data=request.POST)

    next_param = request.GET.get('next', '')


    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next'in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('index'))
    context = {
        'login_form': login_form,
        'next': next_param
    }

    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        register_form = ShopUserRegisterForm
    context = {
        'register_form': register_form
    }
    return render(request, 'authapp/register.html', context)


def edit(request):
    if request.method == 'POST':

        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = {
        'edit_form': edit_form
    }
    return render(request, 'authapp/edit.html', context)









