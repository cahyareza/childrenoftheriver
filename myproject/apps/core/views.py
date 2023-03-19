from django.shortcuts import render
from myproject.apps.events.models import Event

def index(request):
    events = Event.objects.all()

    context = {
        'events': events
    }

    return render(request, 'index.html', context)