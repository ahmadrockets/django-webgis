from django.urls import path, re_path
from apps.authentication import views

urlpatterns = [
    path('login', views.login, name='auth.login'),
    path('register', views.register, name='auth.register'),
    path('logout', views.user_logout, name='auth.logout'),
]