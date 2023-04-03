from django.contrib import admin
from myproject.apps.events.models import Event, Dana, Rekening, Komentar


# Inline
class DanaInline(admin.TabularInline):
    model = Dana


class RekeningInline(admin.TabularInline):
    model = Rekening


class KomentarInline(admin.TabularInline):
    model = Komentar


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [DanaInline, KomentarInline]


@admin.register(Rekening)
class RekeningAdmin(admin.ModelAdmin):
    pass

@admin.register(Komentar)
class KomentarAdmin(admin.ModelAdmin):
    pass