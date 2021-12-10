from django.urls import path, re_path
from apps.admn import views

urlpatterns = [
    path('dashboard', views.dashboard, name='admn.dashboard'),
    path('settingusers', views.settingusersPage, name='admn.settingusers'),
    path('dataumkm', views.dataUmkmPage, name='admn.dataumkm'),
    path('dataproduk', views.dataProdukPage, name='admn.dataproduk'),
]