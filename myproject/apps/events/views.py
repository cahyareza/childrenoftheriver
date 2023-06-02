from django.shortcuts import render, get_object_or_404
from myproject.apps.events.models import Event, Komentar
from .models import Event, KETERANGAN_CHOICES
from .forms import KomentarForm, DanaForm

from django.utils.timezone import now

def event_list(request):
    facets = {
        "categories": {
            "keterangan": KETERANGAN_CHOICES,
        },
    }
    events_mendatang = Event.objects.filter(keterangan='Mendatang')
    events_selesai = Event.objects.filter(keterangan='Selesai')
    if request.GET.get('keterangan'):
        if request.GET.get('keterangan') == 'semua':
            events = Event.objects.all()
        else:
            events = Event.objects.filter(keterangan=request.GET.get('keterangan'))
    else:
        events = Event.objects.all()

    context = {
        'events_mendatang': events_mendatang,
        'events_selesai': events_selesai,
        'events': events,
        'facets': facets,
        'today': now().date(),
    }

    return render(request, 'event/event_list.html', context)

def event_detail(request, slug):
    event = get_object_or_404(Event,slug=slug)
    event_sum = event.event.count()
    komentars = Komentar.objects.all()
    form = KomentarForm(request.POST or None, prefix="form")

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.event = event
            instance.save()

    else:
        form = KomentarForm(prefix="form")

    context = {
        'event': event,
        'form': form,
        'komentars': komentars,
        'event_sum': event_sum
    }

    return render(request, 'event/event_detail.html', context)

def donasi(request):
    if request.method == 'POST':
        form = DanaForm(request.POST or None, prefix="form")
        if form.is_valid():
            instance = form.save(commit=False)
            instance.event = event
            instance.save()

    else:
        form = DanaForm(prefix="form")

    context = {
        'form': form,
    }

    return render(request, 'event/donasi.html', context)