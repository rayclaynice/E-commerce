# Generated by Django 5.0.1 on 2024-01-17 07:31

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=100, scale=None, size=[1000, 500], upload_to='images/'),
        ),
    ]
