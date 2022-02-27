from django.db import models

class Kelurahan(models.Model):
  kelurahan_id = models.AutoField(primary_key=True)
  nama = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
        db_table = "kelurahan"

class JenisUsaha(models.Model):
  jenis_usaha_id = models.AutoField(primary_key=True)
  nama = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
        db_table = "jenis_usaha"

class DataUmkm(models.Model):
  STATUS_DATAUMKM = (
      ("T", "T"),
      ("F", "F"),
      ("X", "X"),
  )
  dataumkm_id = models.AutoField(primary_key=True)
  nama_usaha = models.CharField(max_length=50)
  pemilik = models.CharField(max_length=50, blank=True)
  thn_mulai = models.IntegerField(blank=True)
  alamat = models.CharField(max_length=255, blank=True)
  kelurahan_id = models.IntegerField()
  jenis_usaha_id = models.IntegerField()
  namaproduk = models.CharField(max_length=100, blank=True)
  notelepon = models.CharField(max_length=20, blank=True)
  koordinat = models.CharField(max_length=100, blank=True)
  website = models.CharField(max_length=50, blank=True)
  email = models.CharField(max_length=50, blank=True)
  instagram = models.CharField(max_length=50, blank=True)
  facebook = models.CharField(max_length=50, blank=True)
  twitter = models.CharField(max_length=50, blank=True)
  keterangan = models.CharField(max_length=255, blank=True)
  user_id = models.IntegerField()
  statusverifikasi = models.CharField(max_length=1, choices=STATUS_DATAUMKM, default="F")
  catatan_verifikasi = models.CharField(max_length=255, blank=True)
  verified_at = models.DateTimeField(null=True)
  verified_by = models.IntegerField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
        db_table = "dataumkm"

class DataProduk(models.Model):
  STATUS_PRODUK = (
      ("T", "T"),
      ("F", "F"),
  )
  produk_id = models.AutoField(primary_key=True)
  dataumkm_id = models.IntegerField()
  namaproduk = models.CharField(max_length=100)
  foto = models.CharField(max_length=255, blank=True)
  harga = models.DecimalField(max_digits = 20,decimal_places = 2)
  deskripsi = models.CharField(max_length=255, blank=True)
  status = models.CharField(max_length=1, choices=STATUS_PRODUK, default="F")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
        db_table = "produk"