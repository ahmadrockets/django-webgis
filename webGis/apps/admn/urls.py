from django.urls import path, re_path
from apps.admn import views

urlpatterns = [
    path('dashboard', views.dashboard, name='admn.dashboard'),
    path('settingusers', views.settingusersPage, name='admn.settingusers'),
    path('dataumkm', views.dataUmkmPage, name='admn.dataumkm'),
    
    # api data umkm
    path('umkm', views.createDataUMKM, name='admn.createdataumkm'),
    path('getallumkm', views.getAllUMKM, name='admn.getallumkm'),
    path('getdetailumkm/<int:item_id>', views.getDetailUMKM, name='admn.getdetailumkm'),
    path('updateumkm/<int:item_id>', views.updateDataUMKM, name='admn.updatedataumkm'),
    path('deleteumkm/<int:item_id>', views.deleteDataUMKM, name='admn.deleteumkm'),

    path('dataproduk', views.dataProdukPage, name='admn.dataproduk'),
    path('verifikasiumkm', views.verifikasiUMKMPage, name='admn.verifikasiumkm'),
]