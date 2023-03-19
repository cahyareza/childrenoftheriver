from django.db import models
from myproject.apps.core.mixins import CreationModificationDateBase, UrlBase
from PIL import Image
from django_resized import ResizedImageField
from datetime import datetime
from taggit.managers import TaggableManager


class Event(CreationModificationDateBase, UrlBase):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField(max_length=1000)
    dana = models.CharField(max_length=50)
    tanggal_acara = models.DateField()
    lokasi = models.CharField(max_length=255)
    # kedepan dibuat multiple image
    foto_sebelum = ResizedImageField(scale=0.5, quality=50, upload_to='whatever')
    foto_setelah = ResizedImageField(scale=0.5, quality=50, upload_to='whatever')
    tags = TaggableManager()

    def __str__(self):
        return self.nama

    @property
    def total(self):
        return sum(item.jumlah for item in self.event.all())

    @property
    def remaining_days(self):
        remaining = ( self.tanggal_acara - datetime.now().date()).days
        return remaining


class Rekening(CreationModificationDateBase, UrlBase):
    nama_bank = models.CharField(max_length=100)
    id_bank = models.CharField(max_length=10)
    nomor_rek = models.CharField(max_length=20)
    nama_pemilik = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_bank


class Dana(CreationModificationDateBase, UrlBase):
    event = models.ForeignKey(Event, related_name='event', on_delete=models.CASCADE)
    nama_penyumbang = models.CharField(max_length=50, default="anonymous")
    jumlah = models.IntegerField(default=0)
    ditransfer_ke = models.ForeignKey(Rekening, related_name='rekening', on_delete=models.CASCADE)
    ucapan = models.CharField(max_length=255)
    bukti = ResizedImageField(scale=0.5, quality=50, upload_to='whatever', null=True, blank=True)
