from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.conf import settings
from apps.admn.models import DataUmkm
from apps.admn.models import DataProduk


def index(request):
    gmaps_api = settings.GMAPS_API
    data_umkm = DataUmkm.objects.raw('SELECT dataumkm.*, kelurahan.nama AS kelurahan, jenis_usaha.nama AS jenis_usaha FROM dataumkm  JOIN kelurahan ON kelurahan.kelurahan_id = dataumkm.kelurahan_id JOIN jenis_usaha ON jenis_usaha.jenis_usaha_id = dataumkm.jenis_usaha_id WHERE dataumkm.statusverifikasi="T"')
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
    context = {
        'segment': 'detail_marker',
        'detail_umkm':detail_umkm,
        'data_produk':data_produk
    }
    html_template = loader.get_template('home/detail_marker.html')
    return HttpResponse(html_template.render(context, request))


def about(request):
    context = {'segment': 'about'}

    html_template = loader.get_template('home/about.html')
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
