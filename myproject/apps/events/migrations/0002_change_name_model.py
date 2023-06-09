# Generated by Django 3.2.18 on 2023-03-19 06:17

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_create_events_anad_dana_and_rekenings_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('nama_penyumbang', models.CharField(default='anonymous', max_length=50)),
                ('jumlah', models.IntegerField(default=0)),
                ('ucapan', models.CharField(max_length=255)),
                ('bukti', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=50, scale=0.5, size=[1920, 1080], upload_to='whatever')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='Rekenings',
            new_name='Rekening',
        ),
        migrations.DeleteModel(
            name='Danas',
        ),
        migrations.AddField(
            model_name='dana',
            name='ditransfer_ke',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rekening', to='events.rekening'),
        ),
        migrations.AddField(
            model_name='dana',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='events.event'),
        ),
    ]
