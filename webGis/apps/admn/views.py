from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def dashboard(request):
    context = {'segment': 'dashboard'}

    html_template = loader.get_template('admn/dashboard.html')
    return HttpResponse(html_template.render(context, request))

@login_required
def settingusersPage(request):
    context = {'segment': 'settingusers'}

    html_template = loader.get_template('admn/settingusers.html')
    return HttpResponse(html_template.render(context, request))