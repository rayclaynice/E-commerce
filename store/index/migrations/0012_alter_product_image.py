# Generated by Django 5.0.1 on 2024-01-17 14:56

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=150, scale=0.5, size=[750, 750], upload_to='images/'),
        ),
    ]