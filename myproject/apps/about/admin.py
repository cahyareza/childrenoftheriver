from django.contrib import admin
from myproject.apps.about.models import Profil, Tim

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    pass

@admin.register(Tim)
class TimAdmin(admin.ModelAdmin):
    pass
