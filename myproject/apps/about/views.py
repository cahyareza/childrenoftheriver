from django.shortcuts import render
from .models import Profil, Tim

def about(request):
    return render(request, 'about/about.html')

def profil(request):
    profils = Profil.objects.all()

    context = {
        'profils': profils,
    }
    return render(request, 'about/profil.html', context)

def visi_misi(request):
    profils = Profil.objects.all()

    context = {
        'profils': profils,
    }
    return render(request, 'about/visi_misi.html', context)

def tim(request):
    tims = Tim.objects.all()

    context = {
        'tims': tims,
    }
    return render(request, 'about/tim.html', context)
