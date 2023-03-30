from django.shortcuts import render
from myproject.apps.events.models import Event

def index(request):
    events_mendatang = Event.objects.filter(keterangan='Mendatang')
    events_selesai = Event.objects.filter(keterangan='Selesai')

    context = {
        'events_mendatang': events_mendatang,
        'events_selesai': events_selesai
    }

    return render(request, 'index.html', context)