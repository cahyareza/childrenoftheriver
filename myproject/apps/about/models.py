from django.db import models
from myproject.apps.core.mixins import CreationModificationDateBase, UrlBase

class Profil(CreationModificationDateBase, UrlBase):
    nama = models.CharField(max_length=250)
    tanggal = models.CharField(max_length=50)
    descripsi = models.TextField()

    def __str__(self):
        return self.nama


class Tim(CreationModificationDateBase, UrlBase):
    nama = models.CharField(max_length=250)
    posisi = models.CharField(max_length=50)
    linkedin = models.URLField(max_length=500)
    foto = models.ImageField(null=True, blank=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.nama

    class Meta:
        ordering = ('display_order',)

