from django import forms
from .models import Komentar, Dana, Rekening, Event

class KomentarForm(forms.ModelForm):
    # INFORMASI UNDANGAN
    nama = forms.CharField(
        label='Nama', min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    daerah = forms.CharField(
        label='Daerah', min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Daerah',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    komentar = forms.CharField(
        label='Komentar', min_length=3, max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Komentar',
                'class': 'input',
                'style': 'font-size: 13px',
            }
        )
    )

    class Meta:
        model = Komentar
        fields = ["nama", "daerah", "komentar"]


class DanaForm(forms.ModelForm):

    event = forms.ModelChoiceField(
        queryset=Event.objects.all(),
        widget=forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
        )
    )

    nama_penyumbang = forms.CharField(
        label='Nama', min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama penyumbang',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )
    jumlah = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Jumlah',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    ditransfer_ke = forms.ModelChoiceField(
        queryset=Rekening.objects.all(),
        widget=forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
        )
    )

    ucapan = forms.CharField(
        label='Ucapan', min_length=3, max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ucapan',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    bukti = forms.FileField()

    class Meta:
        model = Komentar
        fields = ["nama_penyumbang", "jumlah", "ditransfer_ke", "ucapan", "bukti"]
