# Generated by Django 3.2.18 on 2023-04-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_add_model_tim'),
    ]

    operations = [
        migrations.AddField(
            model_name='tim',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
