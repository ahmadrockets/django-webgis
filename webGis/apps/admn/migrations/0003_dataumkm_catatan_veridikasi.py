# Generated by Django 3.2.9 on 2022-02-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0002_auto_20220226_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataumkm',
            name='catatan_veridikasi',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]