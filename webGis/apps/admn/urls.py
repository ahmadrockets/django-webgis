from django.urls import path, re_path
from apps.admn import views

urlpatterns = [
    path('dashboard', views.dashboard, name='admn.dashboard'),
    path('settingusers', views.settingusersPage, name='admn.settingusers'),

    # Data UMKM
    path('dataumkm', views.dataUmkmPage, name='admn.dataumkm'),
    path('umkm', views.createDataUMKM, name='admn.createdataumkm'),
    path('getallumkm', views.getAllUMKM, name='admn.getallumkm'),
    path('getdetailumkm/<int:item_id>', views.getDetailUMKM, name='admn.getdetailumkm'),
    path('updateumkm/<int:item_id>', views.updateDataUMKM, name='admn.updatedataumkm'),
    path('deleteumkm/<int:item_id>', views.deleteDataUMKM, name='admn.deleteumkm'),

    # Data Produk
    path('dataproduk', views.dataProdukPage, name='admn.dataproduk'),
    path('produk', views.createProduk, name='admn.createdataproduk'),
    path('getdetailproduk/<int:item_id>', views.getDetailProduct, name='admn.getdetailproduct'),
    path('updateproduk/<int:item_id>', views.updateDataProduk, name='admn.updatedataproduk'),
    path('deleteproduk/<int:item_id>', views.deleteDataProduk, name='admn.deleteproduk'),
    
    path('verifikasiumkm', views.verifikasiUMKMPage, name='admn.verifikasiumkm'),
]