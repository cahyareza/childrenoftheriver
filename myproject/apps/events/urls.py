from django.urls import path
from .views import event_list, event_detail, donasi

urlpatterns = [
    path('', event_list, name='event_list'),
    path('donasi', donasi, name='donasi'),
    path('<slug:slug>', event_detail, name='event_detail'),
]