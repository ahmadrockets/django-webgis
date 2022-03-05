from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignUpForm


def login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_aktif == 'T':
                    auth_login(request, user)
                    return redirect("/")
                else:
                    msg = 'User is not active, please contact Administrator'
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "authentication/login.html", {"form": form, "msg": msg})

@login_required
def user_logout(request):
    logout(request)
    return redirect("/auth/login")

def register(request):
    context = {'segment': 'register'}
    form = SignUpForm(request.POST or None)
    msg = None

    return render(request, "authentication/register.html", {"form": form, "msg": msg})
