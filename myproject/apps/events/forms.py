from django import forms
from django.utils.translation import ugettext_lazy as _
from django.db import models
from myproject.apps.events.models import Event, KETERANGAN_CHOICES

class EventFilterForm(forms.Form):
    keterangan = forms.ChoiceField(
        label=_("Keterangan"), required=False, choices=KETERANGAN_CHOICES
    )
