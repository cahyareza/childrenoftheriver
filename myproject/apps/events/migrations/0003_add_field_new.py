# Generated by Django 3.2.18 on 2023-03-20 01:40

import datetime
from django.db import migrations, models
import django_resized.forms
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('events', '0002_change_name_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='event',
            name='tanggal_donasi_selesai',
            field=models.DateField(default=datetime.datetime(2023, 3, 20, 8, 40, 43, 822798)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dana',
            name='bukti',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=50, scale=0.5, size=[1920, 1080], upload_to='whatever'),
        ),
    ]
