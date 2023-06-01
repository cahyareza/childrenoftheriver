from django.urls import path
from .views import list, detail

urlpatterns = [
    path('', list, name='list'),
    # path('donasi', donasi, name='donasi'),
    path('<slug:category_slug>/<slug:slug>/', detail, name='detail'),
]