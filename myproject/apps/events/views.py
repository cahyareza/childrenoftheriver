from django.shortcuts import render
from myproject.apps.events.models import Event

from .forms import EventFilterForm
from .models import Event, KETERANGAN_CHOICES

def event(request):
    facets = {
        "categories": {
            "keterangan": KETERANGAN_CHOICES,
        },
    }
    events_mendatang = Event.objects.filter(keterangan='Mendatang')
    events_selesai = Event.objects.filter(keterangan='Selesai')
    events = Event.objects.all()

    context = {
        'events_mendatang': events_mendatang,
        'events_selesai': events_selesai,
        'events': events,
        'facets': facets,
    }

    return render(request, 'event/event_list.html', context)

def event_list(request):
    qs = Event.objects.order_by("nama")
    form = EventFilterForm(data=request.GET)

    facets = {
        "selected": {},
        "categories": {
            "keterangan": KETERANGAN_CHOICES,
        },
    }

    if form.is_valid():
        filters = (
            # query parameter, filter parameter
            ("keterangan", "keterangan"),
        )
        qs = filter_facets(facets, qs, form, filters)

    context = {"form": form, "facets": facets, "object_list": qs}

    return render(request, 'event/event_list.html', context)

def filter_facets(facets, qs, form, filters):
    for query_param, filter_param in filters:
        value = form.cleaned_data[query_param]
        if value:
            selected_value = value
            if query_param == "keterangan":
                keterangan = int(value)
                selected_value = (keterangan, dict(KETERANGAN_CHOICES)[keterangan])
            facets["selected"][query_param] = selected_value
            filter_args = {filter_param: value}
            qs = qs.filter(**filter_args).distinct()
    return qs