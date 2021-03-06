# Generated by Django 3.2.9 on 2022-03-05 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataProduk',
            fields=[
                ('produk_id', models.AutoField(primary_key=True, serialize=False)),
                ('dataumkm_id', models.IntegerField()),
                ('namaproduk', models.CharField(max_length=100)),
                ('foto', models.CharField(blank=True, max_length=255)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=20)),
                ('deskripsi', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('T', 'T'), ('F', 'F')], default='F', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'produk',
            },
        ),
        migrations.CreateModel(
            name='DataUmkm',
            fields=[
                ('dataumkm_id', models.AutoField(primary_key=True, serialize=False)),
                ('nama_usaha', models.CharField(max_length=50)),
                ('pemilik', models.CharField(blank=True, max_length=50)),
                ('thn_mulai', models.IntegerField(blank=True)),
                ('alamat', models.CharField(blank=True, max_length=255)),
                ('kelurahan_id', models.IntegerField()),
                ('jenis_usaha_id', models.IntegerField()),
                ('namaproduk', models.CharField(blank=True, max_length=100)),
                ('notelepon', models.CharField(blank=True, max_length=20)),
                ('koordinat', models.CharField(blank=True, max_length=100)),
                ('website', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('keterangan', models.CharField(blank=True, max_length=255)),
                ('user_id', models.IntegerField()),
                ('statusverifikasi', models.CharField(choices=[('T', 'T'), ('F', 'F'), ('X', 'X')], default='F', max_length=1)),
                ('catatan_verifikasi', models.CharField(blank=True, max_length=255)),
                ('verified_at', models.DateTimeField(null=True)),
                ('verified_by', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'dataumkm',
            },
        ),
        migrations.CreateModel(
            name='JenisUsaha',
            fields=[
                ('jenis_usaha_id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'jenis_usaha',
            },
        ),
        migrations.CreateModel(
            name='Kelurahan',
            fields=[
                ('kelurahan_id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'kelurahan',
            },
        ),
    ]
