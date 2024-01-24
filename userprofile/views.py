# -*- coding: utf-8 -*-
from cssutils import _
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm  # Assuming the forms module is in the same directory
from ticketsystem.views import view_dashboard
from django.shortcuts import redirect

def loginview(request):
    state = ("Enter Username and Password...")
    username = password = ''
    form = LoginForm()
    department = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/ticketsystem/mytickets")

        state = _("Invalid Username or Password!!")

    return render(request, 'userprofile/index.html', {'form': form, 'state': state})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("loginview"))
