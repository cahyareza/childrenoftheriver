from django.contrib import admin
from myproject.apps.events.models import Event, Dana, Rekening


# Inline
class DanaInline(admin.TabularInline):
    model = Dana


class RekeningInline(admin.TabularInline):
    model = Rekening


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [DanaInline,]


@admin.register(Rekening)
class RekeningAdmin(admin.ModelAdmin):
    pass