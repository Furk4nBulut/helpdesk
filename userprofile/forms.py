# -*- coding: utf-8 -*-
from django import forms

from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(label=_("Username"), max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'placeholder': 'password'}))