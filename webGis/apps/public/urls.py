from django.urls import path, re_path
from apps.public import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('getdetailmarker/<int:item_id>', views.detailMarker, name='admn.detailmarker'),
    path('getdetailmarkerposition/<int:item_id>', views.detailMarkerPosition, name='admn.detailmarkerposition'),

    path('about', views.about, name='about'),

]
