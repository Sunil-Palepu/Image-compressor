# Generated by Django 4.2.7 on 2023-11-17 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0005_compressedimage_height_compressedimage_width'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compressedimage',
            name='height',
        ),
        migrations.RemoveField(
            model_name='compressedimage',
            name='width',
        ),
    ]