from django.urls import path
from .views import about, profil, visi_misi, tim

urlpatterns = [
    path('', about, name='about'),
    path('profil/', profil, name='profil'),
    path('visi/', visi_misi, name='visi_misi'),
    path('tim/', tim, name='tim'),
]