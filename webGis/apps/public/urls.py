from django.urls import path, re_path
from apps.public import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('about', views.about, name='about'),

]
