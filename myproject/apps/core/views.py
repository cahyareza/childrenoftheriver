import random

from django.shortcuts import render
from myproject.apps.events.models import Event
from myproject.apps.blog.models import Post

from django.utils.timezone import now

def index(request):
    events_mendatang = Event.objects.filter(keterangan='Mendatang')[0:3]
    events_selesai = Event.objects.filter(keterangan='Selesai')

    related_posts = list(Post.objects.filter(status=Post.ACTIVE))[0:4]
    if len(related_posts) >=3:
        related_posts = random.sample(related_posts, 3)

    context = {
        'events_mendatang': events_mendatang,
        'events_selesai': events_selesai,
        'related_posts': related_posts,
        'today': now().date(),
    }

    return render(request, 'index.html', context)