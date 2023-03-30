from django.urls import path
from .views import event, event_list

urlpatterns = [
    path('', event, name='event'),
    path('list/', event_list, name='event_list'),
]