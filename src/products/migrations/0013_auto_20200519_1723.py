# Generated by Django 3.0.5 on 2020-05-19 17:23

import django.core.files.storage
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20200519_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/egonsaks/Documents/digital_marketplace/static_cdn/protected'), upload_to=products.models.download_media_location),
        ),
    ]
