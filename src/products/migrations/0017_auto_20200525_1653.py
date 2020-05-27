# Generated by Django 3.0.5 on 2020-05-25 16:53

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20200524_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='type',
            field=models.CharField(choices=[('hd', 'HD'), ('sd', 'SD'), ('micro', 'Micro')], default='hd', max_length=20),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='media',
            field=models.ImageField(blank=True, height_field='height', null=True, upload_to=products.models.thumbnail_location, width_field='width'),
        ),
    ]