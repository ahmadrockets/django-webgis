from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.conf import settings
from apps.admn.models import DataUmkm
from apps.admn.models import DataProduk
from django.http import JsonResponse
import json


def index(request):
    gmaps_api = settings.GMAPS_API
    
    s_umkm = request.GET.get('s_umkm', '')

    if s_umkm != '':
        data_umkm = DataUmkm.objects.filter( nama_usaha__icontains=s_umkm, statusverifikasi__exact='T' ).exclude(koordinat__isnull=True).exclude(koordinat__exact='')
        # query = "SELECT dataumkm.*, kelurahan.nama AS kelurahan, jenis_usaha.nama AS jenis_usaha FROM dataumkm  JOIN kelurahan ON kelurahan.kelurahan_id = dataumkm.kelurahan_id JOIN jenis_usaha ON jenis_usaha.jenis_usaha_id = dataumkm.jenis_usaha_id WHERE dataumkm.statusverifikasi='T' AND dataumkm.nama_usaha like '%%%s%%'" % (s_umkm)
    else:
        data_umkm = DataUmkm.objects.filter(statusverifikasi__exact='T' ).exclude(koordinat__isnull=True).exclude(koordinat__exact='')

    context = {
        'segment': 'home',
        'gmaps_api': gmaps_api,
        'data_umkm': data_umkm
    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

def detailMarker(request, item_id):
    detail_umkm = DataUmkm.objects.raw(f'SELECT dataumkm.*, kelurahan.nama AS kelurahan, jenis_usaha.nama AS jenis_usaha FROM dataumkm  JOIN kelurahan ON kelurahan.kelurahan_id = dataumkm.kelurahan_id JOIN jenis_usaha ON jenis_usaha.jenis_usaha_id = dataumkm.jenis_usaha_id WHERE dataumkm.statusverifikasi="T" AND dataumkm.dataumkm_id={item_id}')[0]
    data_produk = DataProduk.objects.raw(f'SELECT produk.*, dataumkm.nama_usaha FROM produk JOIN dataumkm ON dataumkm.dataumkm_id = produk.dataumkm_id WHERE produk.dataumkm_id = {item_id} AND produk.status="T"')
    link_wa = ""
    if detail_umkm.notelepon !="":
        if detail_umkm.notelepon[0:2]=="08":
            link_wa = "62"+detail_umkm.notelepon[1:]

    context = {
        'segment': 'detail_marker',
        'detail_umkm':detail_umkm,
        'data_produk':data_produk,
        'link_wa':link_wa
    }
    html_template = loader.get_template('home/detail_marker.html')
    return HttpResponse(html_template.render(context, request))

def detailMarkerPosition(request, item_id):
    response = {}
    status = 400
    try : 
        item    = DataUmkm.objects.get(dataumkm_id=item_id)
        dataItem = {
            'nama_usaha' : item.nama_usaha,
            'pemilik' : item.pemilik,
            'koordinat' : item.koordinat,
        }
        response = {
            'status':'success',
            'message': 'Success get data umkm',
            'item' : dataItem
        }
        status = 200
    except Exception as e:
        response = {
            'status':'failed',
            'message': f'data not found {e}',
            'item':{}
        }
        status = 400
        
    return JsonResponse(response, status=status)


def about(request):
    context = {'segment': 'about'}

    html_template = loader.get_template('home/about.html')
    return HttpResponse(html_template.render(context, request))

def unauthorized(request):
    context = {'segment': 'unauthorized'}

    html_template = loader.get_template('home/unauthorized.html')
    return HttpResponse(html_template.render(context, request))

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
