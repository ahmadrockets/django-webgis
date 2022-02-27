from django import template
from django.http import JsonResponse
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import DataUmkm
from .models import Kelurahan
from .models import JenisUsaha
from .models import DataProduk
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import os
from django.conf import settings
import datetime

@login_required
def dashboard(request):
    data_dashboard = Kelurahan.objects.raw('SELECT *, (SELECT COUNT(*) AS jml FROM dataumkm WHERE dataumkm.kelurahan_id=kelurahan.kelurahan_id AND dataumkm.statusverifikasi="T") AS jml FROM kelurahan')
    context = {
        'segment': 'dashboard',
        'data_dashboard': data_dashboard
    }

    html_template = loader.get_template('admn/dashboard.html')
    return HttpResponse(html_template.render(context, request))

@login_required
def settingusersPage(request):
    context = {'segment': 'settingusers'}

    html_template = loader.get_template('admn/settingusers.html')
    return HttpResponse(html_template.render(context, request))

@login_required
def dataUmkmPage(request):
    data_umkm = DataUmkm.objects.raw('SELECT dataumkm.*, kelurahan.nama AS kelurahan, jenis_usaha.nama AS jenis_usaha FROM dataumkm  JOIN kelurahan ON kelurahan.kelurahan_id = dataumkm.kelurahan_id JOIN jenis_usaha ON jenis_usaha.jenis_usaha_id = dataumkm.jenis_usaha_id')
    data_kelurahan = Kelurahan.objects.all()
    data_jenisusaha = JenisUsaha.objects.all()
    context = {
        'segment': 'dataumkm', 
        'subsegment':'dataumkm',
        'data_kelurahan' : data_kelurahan,
        'data_jenisusaha' : data_jenisusaha,
        'data_umkm' : data_umkm,
    }

    html_template = loader.get_template('admn/dataumkm.html')
    return HttpResponse(html_template.render(context, request))

# api data umkm
@login_required
@method_decorator(csrf_exempt, name='dispatch')
@require_http_methods(["POST"])
def createDataUMKM(request):
    data = json.loads(request.body.decode("utf-8"))
    user_login = request.user

    p_nama_usaha = data.get('nama_usaha')
    p_pemilik = data.get('pemilik')
    p_thn_mulai = data.get('thn_mulai')
    p_alamat = data.get('alamat')
    p_kelurahan_id = data.get('kelurahan_id')
    p_jenis_usaha_id = data.get('jenis_usaha_id')
    p_namaproduk = data.get('namaproduk')
    p_notelepon = data.get('notelepon')
    p_koordinat = data.get('koordinat')
    p_website = data.get('website')
    p_email = data.get('email')
    p_instagram = data.get('instagram')
    p_facebook = data.get('facebook')
    p_twitter = data.get('twitter')
    p_keterangan = data.get('keterangan')

    umkm_data = {
        'nama_usaha' : p_nama_usaha,
        'pemilik' : p_pemilik,
        'thn_mulai' : p_thn_mulai,
        'alamat' : p_alamat,
        'kelurahan_id' : p_kelurahan_id,
        'jenis_usaha_id' : p_jenis_usaha_id,
        'namaproduk' : '',
        'notelepon' : p_notelepon,
        'koordinat' : p_koordinat,
        'website' : p_website,
        'email' : p_email,
        'instagram' : p_instagram,
        'facebook' : p_facebook,
        'twitter' : p_twitter,
        'keterangan' : p_keterangan,
        'statusverifikasi' : 'T' if (user_login.id==1) else 'F',
        'user_id' : user_login.id,
    }
    data = {}
    status = 400
    try:
        dataumkm_item = DataUmkm.objects.create(**umkm_data)
        data = {
            "status": "success",
            # "message": f"New umkm added to database with id: {dataumkm_item.id}"
            "message": "New umkm added to database"
        }
        status = 201 
    except Exception as e:
        data = {
            "status": "failed",
            "message": f"failed to save data to database {e}"
        }
        status = 400
    return JsonResponse(data, status=status)

@login_required
@require_http_methods(["GET"])
def getAllUMKM(request):
    items_count = DataUmkm.objects.count()
    items = DataUmkm.objects.all()
    items_data = []
    for item in items:
        items_data.append({
            'nama_usaha' : item.nama_usaha,
            'pemilik' : item.pemilik,
            'thn_mulai' : item.thn_mulai,
            'alamat' : item.alamat,
            'kelurahan_id' : item.kelurahan_id,
            'jenis_usaha_id' : item.jenis_usaha_id,
            'namaproduk' : item.namaproduk,
            'notelepon' : item.notelepon,
            'koordinat' : item.koordinat,
            'website' : item.website,
            'email' : item.email,
            'instagram' : item.instagram,
            'facebook' : item.facebook,
            'twitter' : item.twitter,
            'keterangan' : item.keterangan,
            'statusverifikasi' : item.statusverifikasi,
        })
    data = {
        'items': items_data,
        'count': items_count,
    }
    return JsonResponse(data)

@login_required
@method_decorator(csrf_exempt, name='dispatch')
@require_http_methods(["GET"])
def getDetailUMKM(request, item_id):
    response = {}
    status = 400
    try : 
        item    = DataUmkm.objects.get(dataumkm_id=item_id)
        dataItem = {
            'nama_usaha' : item.nama_usaha,
            'pemilik' : item.pemilik,
            'thn_mulai' : item.thn_mulai,
            'alamat' : item.alamat,
            'kelurahan_id' : item.kelurahan_id,
            'jenis_usaha_id' : item.jenis_usaha_id,
            'namaproduk' : item.namaproduk,
            'notelepon' : item.notelepon,
            'koordinat' : item.koordinat,
            'website' : item.website,
            'email' : item.email,
            'instagram' : item.instagram,
            'facebook' : item.facebook,
            'twitter' : item.twitter,
            'keterangan' : item.keterangan,
            'statusverifikasi' : item.statusverifikasi,
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

@login_required
@method_decorator(csrf_exempt, name='dispatch')
@require_http_methods(["PATCH"])
def updateDataUMKM(request, item_id):
    data = json.loads(request.body.decode("utf-8"))

    response = {}
    status = 400

    try : 
        item                    = DataUmkm.objects.get(dataumkm_id=item_id)

        item.nama_usaha         = data['nama_usaha']
        item.pemilik            = data['pemilik']
        item.thn_mulai          = data['thn_mulai']
        item.alamat             = data['alamat']
        item.kelurahan_id       = data['kelurahan_id']
        item.jenis_usaha_id     = data['jenis_usaha_id']
        item.notelepon          = data['notelepon']
        item.koordinat          = data['koordinat']
        item.website            = data['website']
        item.email              = data['email']
        item.instagram          = data['instagram']
        item.facebook           = data['facebook']
        item.twitter            = data['twitter']
        item.keterangan         = data['keterangan']
        item.save()
        response = {
            'status':'success',
            'message': f'Item {item_id} has been updated'
        }
        status = 200
    except Exception as e:
        response = {
            'status':'failed',
            'message': f'failed update data {e}'
        }
        status = 400

    return JsonResponse(response, status=status)

@login_required
@method_decorator(csrf_exempt, name='dispatch')
@require_http_methods(["DELETE"])
def deleteDataUMKM(request, item_id):
    response = {}
    status = 400
    try : 
        item     = DataUmkm.objects.get(dataumkm_id=item_id)
        item.delete()
        response = {
            'status':'success',
            'message': f'Item {item_id} has been deletd'
        }
        status = 200
    except Exception as e:
        response = {
            'status':'failed',
            'message': f'failed delete data {e}'
        }
        status = 400

    return JsonResponse(response, status=status)

@login_required
def dataProdukPage(request):
    # search UMKM
    search_umkm = request.POST.get('search_umkm')
    data_umkm = DataUmkm.objects.all()
    
    data_produk = {}
    if search_umkm != "" and search_umkm != None:
        data_produk = DataProduk.objects.raw(f'SELECT produk.*, dataumkm.nama_usaha FROM produk JOIN dataumkm ON dataumkm.dataumkm_id = produk.dataumkm_id WHERE produk.dataumkm_id = {search_umkm}')

    context = {
        'segment': 'dataumkm', 
        'subsegment':'dataproduk',
        'data_umkm':data_umkm,
        'data_produk':data_produk,
        'search_umkm':search_umkm
    }

    html_template = loader.get_template('admn/dataproduk.html')
    return HttpResponse(html_template.render(context, request))

# API Data Produk
@login_required
@method_decorator(csrf_exempt, name='dispatch')
@require_http_methods(["POST"])
def createProduk(request):
    p_umkm = request.POST.get('umkm', '')
    p_nama_produk = request.POST.get('nama_produk', '')
    p_keterangan = request.POST.get('keterangan', '')
    p_harga = request.POST.get('harga', '')
    p_gambar = ""
    p_status = request.POST.get('status', '')

    # upload function
    timenow = datetime.datetime.now().strftime('%d%m%Y%H%I%S')
    img = request.FILES.get('gambar', False)

    if img :
        img_extension = os.path.splitext(img.name)[1]
        image_folder = 'apps/static/images/'
        if not os.path.exists(image_folder):
            os.mkdir(image_folder)

        img_save_path = image_folder+"produk_"+p_umkm+"_"+timenow+img_extension
        with open(img_save_path, 'wb+') as f:
            for chunk in img.chunks():
                f.write(chunk)
        
        p_gambar = img_save_path

    product_data = {
        'dataumkm_id': p_umkm,
        'namaproduk': p_nama_produk,
        'foto': p_gambar,
        'harga': p_harga,
        'deskripsi': p_keterangan,
        'status': p_status,
    }
    data = {}
    status = 400
    try:
        produk_item = DataProduk.objects.create(**product_data)
        data = {
            "status": "success",
            # "message": f"New prodyct added to database with id: {produk_item.id}"
            "message": "New product added to database"
        }
        status = 201 
    except Exception as e:
        data = {
            "status": "failed",
            "message": f"failed to save data to database {e}"
        }
        status = 400
    return JsonResponse(data, status=status)

@login_required
@method_decorator(csrf_exempt, name='dispatch')
@require_http_methods(["GET"])
def getDetailProduct(request, item_id):
    response = {}
    status = 400
    try : 
        item    = DataProduk.objects.get(produk_id=item_id)
        dataItem = {
            'dataumkm_id' : item.dataumkm_id,
            'namaproduk' : item.namaproduk,
            'foto' : item.foto,
            'harga' : item.harga,
            'deskripsi' : item.deskripsi,
            'status' : item.status,
        }
        response = {
            'status':'success',
            'message': 'Success get data product',
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

@login_required
@method_decorator(csrf_exempt, name='dispatch')
@require_http_methods(["POST"])
def updateDataProduk(request, item_id):
    p_umkm = request.POST.get('umkm', '')
    p_nama_produk = request.POST.get('nama_produk', '')
    p_keterangan = request.POST.get('keterangan', '')
    p_harga = request.POST.get('harga', '')
    p_gambar = request.POST.get('gambar_edit', '')
    p_status = request.POST.get('status', '')

    # upload function
    timenow = datetime.datetime.now().strftime('%d%m%Y%H%I%S')
    img = request.FILES.get('gambar', False)

    if img :
        img_extension = os.path.splitext(img.name)[1]
        image_folder = 'apps/static/images/'
        if not os.path.exists(image_folder):
            os.mkdir(image_folder)

        img_save_path = image_folder+"produk_"+p_umkm+"_"+timenow+img_extension
        with open(img_save_path, 'wb+') as f:
            for chunk in img.chunks():
                f.write(chunk)
        
        p_gambar = img_save_path

    response = {}
    status = 400

    try : 
        item              = DataProduk.objects.get(produk_id=item_id)
        item.dataumkm_id  = p_umkm
        item.namaproduk   = p_nama_produk
        item.foto         = p_gambar
        item.harga        = p_harga
        item.deskripsi    = p_keterangan
        item.status       = p_status
        item.save()
        response = {
            'status':'success',
            'message': f'Item {item_id} has been updated'
        }
        status = 200
    except Exception as e:
        response = {
            'status':'failed',
            'message': f'failed update data {e}'
        }
        status = 400

    return JsonResponse(response, status=status)

@login_required
@method_decorator(csrf_exempt, name='dispatch')
@require_http_methods(["DELETE"])
def deleteDataProduk(request, item_id):
    response = {}
    status = 400
    try : 
        item     = DataProduk.objects.get(produk_id=item_id)
        
        # Delete file
        if item.foto != "":
            if os.path.isfile(item.foto):
                os.remove(item.foto)


        item.delete()
        response = {
            'status':'success',
            'message': f'Item {item_id} has been deletd'
        }
        status = 200
    except Exception as e:
        response = {
            'status':'failed',
            'message': f'failed delete data {e}'
        }
        status = 400

    return JsonResponse(response, status=status)

@login_required
def verifikasiUMKMPage(request):
    data_umkm = DataUmkm.objects.raw('SELECT dataumkm.*, auth_user.username FROM dataumkm LEFT JOIN auth_user ON dataumkm.user_id = auth_user.id WHERE statusverifikasi = "F"')
    data_kelurahan = Kelurahan.objects.all()
    data_jenisusaha = JenisUsaha.objects.all()
    context = {
        'segment': 'dataumkm', 
        'subsegment':'verifikasiumkm',
        'data_umkm':data_umkm,
        'data_kelurahan' : data_kelurahan,
        'data_jenisusaha' : data_jenisusaha
    }

    html_template = loader.get_template('admn/verifikasiumkm.html')
    return HttpResponse(html_template.render(context, request))


@login_required
@method_decorator(csrf_exempt, name='dispatch')
@require_http_methods(["POST"])
def doVerifikasiUMKM(request, item_id):
    user_login = request.user
    response = {}
    status = 400
    try : 
        item                    = DataUmkm.objects.get(dataumkm_id=item_id)
        item.statusverifikasi   = 'T'
        item.verified_at        = datetime.datetime.now().strftime('%Y-%m-%d %H:%I:%S')
        item.verified_by        = user_login.id
        item.save()
        response = {
            'status':'success',
            'message': f'Item {item_id} has been verified'
        }
        status = 200
    except Exception as e:
        response = {
            'status':'failed',
            'message': f'failed verif data {e}'
        }
        status = 400

    return JsonResponse(response, status=status)

@login_required
@method_decorator(csrf_exempt, name='dispatch')
@require_http_methods(["POST"])
def doTolakUMKM(request, item_id):
    user_login = request.user
    data = json.loads(request.body.decode("utf-8"))
    response = {}
    status = 400
    try : 
        item                    = DataUmkm.objects.get(dataumkm_id=item_id)
        item.statusverifikasi   = 'X'
        item.catatan_verifikasi = data['alasan_penolakan']
        item.verified_at        = datetime.datetime.now().strftime('%Y-%m-%d %H:%I:%S')
        item.verified_by        = user_login.id
        item.save()
        response = {
            'status':'success',
            'message': f'Item {item_id} has been verified'
        }
        status = 200
    except Exception as e:
        response = {
            'status':'failed',
            'message': f'failed verif data {e}'
        }
        status = 400

    return JsonResponse(response, status=status)