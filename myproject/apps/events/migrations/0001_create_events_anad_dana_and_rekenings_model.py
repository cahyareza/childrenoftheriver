# Generated by Django 3.2.18 on 2023-03-19 06:11

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('nama', models.CharField(max_length=255)),
                ('deskripsi', models.TextField(max_length=1000)),
                ('dana', models.CharField(max_length=50)),
                ('tanggal_acara', models.DateField()),
                ('lokasi', models.CharField(max_length=255)),
                ('foto_sebelum', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=50, scale=0.5, size=[1920, 1080], upload_to='whatever')),
                ('foto_setelah', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=50, scale=0.5, size=[1920, 1080], upload_to='whatever')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rekenings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('nama_bank', models.CharField(max_length=100)),
                ('id_bank', models.CharField(max_length=10)),
                ('nomor_rek', models.CharField(max_length=20)),
                ('nama_pemilik', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Danas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('nama_penyumbang', models.CharField(default='anonymous', max_length=50)),
                ('jumlah', models.IntegerField(default=0)),
                ('ucapan', models.CharField(max_length=255)),
                ('bukti', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=50, scale=0.5, size=[1920, 1080], upload_to='whatever')),
                ('ditransfer_ke', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rekenings', to='events.rekenings')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.events')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
