# Generated by Django 3.2.9 on 2022-03-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_is_aktif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_aktif',
            field=models.CharField(choices=[('T', 'T'), ('F', 'F'), ('P', 'P')], default='F', max_length=1),
        ),
    ]
