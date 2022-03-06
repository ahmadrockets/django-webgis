# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    nama = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nama",
                "class": "form-control",
                "id": "reg_nama"
            }
        ))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
                "id": "reg_username"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
                "id": "reg_email"
            }
        ))
    notelp = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nomor Telepon / HP",
                "class": "form-control",
                "id": "reg_notelp"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                "id": "reg_password"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control",
                "id": "reg_repassword"
            }
        ))

    class Meta:
        model = User
        fields = ('nama', 'username', 'email', 'notelp', 'password1', 'password2')
